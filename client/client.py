import random
import socket
import select
import pickle
from threading import Thread, RLock
import numpy
from PyQt5 import QtCore, QtGui, QtWidgets
import lobby_ui
import game_ui

element_dict = {
    0:'Arcane',
    1:'Feu',
    2:'Eau',
    3:'Air',
    4:'Chaos'
}

lock = RLock()


class Carte:  
    def __init__(self, e, n): # Carte avec e élement et n nombre
        self.element = e
        self.nombre = n
        self.delete = False
        self.shown = False

    def make_widget(self, hbox):
        self.widget = QtWidgets.QPushButton()
        self.widget.setFixedSize(100,140)
        self.widget.setIcon(QtGui.QIcon(QtGui.QPixmap("image/cards/{}_".format(element_dict[self.element]) + str(self.nombre) + ".png")))
        self.widget.setIconSize(QtCore.QSize(100,140))
        self.widget.clicked.connect(lambda: self.delete_widget(hbox))
        hbox.addWidget(self.widget)
        self.shown = True

    def delete_widget(self, hbox):
        global hand
        hbox.removeWidget(self.widget)
        self.widget.deleteLater()
        self.delete = True
        self.shown = False
        hand.clean()

    def __repr__(self):
        return element_dict[self.element] + " " + str(self.nombre)

class Deck: # Deck assemblage de carte
    

    def __init__(self):
        self.deck = []

    def append(self, c):
        self.deck.append(c)
    
    def pop(self, i=-1):
        self.deck.pop(i)

    def clean(self):
        global connexion
        global name

        del_list = []
        for i in range(len(self.deck)):
            if self.deck[i].delete:
                with lock:
                    cmd = "/discard " + name + " {}".format(i)
                    connexion.send(cmd.encode())
                    del_list.append(i)
        for i in del_list:
            self.pop(i)

    def suffle(self):
        random.shuffle(self.deck)

    def show(self, n):
        return [self.deck[-i] for i in range(min(len(self.deck), n))]

    def __repr__(self):
        chaine = ""
        for c in self.deck:
            chaine += "     {}\n".format(str(c))
        return chaine


class LobbyWindow(QtWidgets.QMainWindow):
    
    
    switch_window = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = lobby_ui.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.connect_pushButton.clicked.connect(self.connect)

    def connect(self):
        global name
        global d_name
        global ip
        global port
        global connexion
        global hand
        global terminal_thread

        d_name = self.ui.name_lineEdit.text()
        name = ""
        for c in d_name:
            if c == " ":
                name += "_"
            else:
                name += c
        ip = self.ui.ip_lineEdit.text()
        port = self.ui.port_lineEdit.text()


        try:
            connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connexion.connect((ip, int(port)))

            print(connexion)
            if self.ui.deck_checkBox.isChecked:
                pdeck = ""
                for n in self.ui.case:
                    pdeck += "{};".format(str(n.value()))
                pdeck = pdeck[0:-1]
                c_msg = "/connect {} ".format(name) + pdeck

            else:
                c_msg = "/connect {}".format(name)

            with lock:
                connexion.send(c_msg.encode())
                if connexion.recv(4096) == b"load profile":
                    content = connexion.recv(32768)
                    global hand
                    hand = pickle.loads(content)

            alert = QtWidgets.QMessageBox()
            alert.setWindowTitle("Connection")
            alert.setText("Connection réussie !")
            alert.exec_()

            terminal_thread = Terminal()
            terminal_thread.daemon = True
            terminal_thread.start()

            self.ui.connect_pushButton.setEnabled(False)
        except ValueError:
            alert = QtWidgets.QMessageBox()
            alert.setIcon(QtWidgets.QMessageBox.Critical)
            alert.setWindowTitle("Erreur")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icon\effacer.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
            alert.setWindowIcon(icon)
            alert.setText("Valeurs invalides.")
            alert.exec_()
        except (ConnectionRefusedError, ConnectionError, ConnectionAbortedError):
            alert = QtWidgets.QMessageBox()
            alert.setIcon(QtWidgets.QMessageBox.Critical)
            alert.setWindowTitle("Erreur")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("image\icon\effacer.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
            alert.setWindowIcon(icon)
            alert.setText("Connection impossible")
            alert.exec_()

        

    def switch_lobby(self):
        self.switch_window.emit()

class GameWindow(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()
    refresh_cards = QtCore.pyqtSignal()
    view_signal = QtCore.pyqtSignal()
    empty_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = game_ui.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.drawenv_pushButton.clicked.connect(lambda : self.draw("env"))
        self.ui.drawdeck_pushButton.clicked.connect(lambda : self.draw("own"))

        self.ui.seeenv_pushButton.clicked.connect(lambda : self.view(self.ui.seeenv_spinBox.value(), "env"))
        self.ui.seedeck_pushButton.clicked.connect(lambda : self.view(self.ui.seedeck_spinBox.value(), "own"))

    def draw(self, deck):
        global name
        global connexion

        dcmd = "/draw " + name + " " + deck
        connexion.send(dcmd.encode())

    def view(self, n, deck):
        global name
        global connexion
        if n != 0:
            cmd = "/view " + name + " " + deck + " " + str(n)
            connexion.send(cmd.encode())

    def view_box(self, deck):
        alert = QtWidgets.QMessageBox()
        alert.setIcon(QtWidgets.QMessageBox.Information)
        alert.setWindowTitle("Cartes")
        alert.setText(str(deck))

        alert.exec_()

    def empty_box(self):
        alert = QtWidgets.QMessageBox()
        alert.setIcon(QtWidgets.QMessageBox.Critical)
        alert.setWindowTitle("Erreur")
        alert.setText("Pas assez de cartes.")
        alert.exec_()

    def ref_cards(self):
        for c in hand.deck:
            if not c.shown and not c.delete:
                c.make_widget(self.ui.hbox)

    def switch_game(self):
        self.switch_window.emit()

class Controller:
    def __init__(self):
        pass

    def show_lobby(self):
        self.lobby = LobbyWindow()
        self.lobby.switch_window.connect(self.show_game)
        self.lobby.show()
        try:
            self.game.close()
        except:
            pass

    def show_game(self):
        global d_name
        self.game = GameWindow()
        self.game.setWindowTitle("JDR 13 - {}".format(d_name))
        self.game.ref_cards()
        self.game.switch_window.connect(self.game.close)
        self.game.refresh_cards.connect(self.game.ref_cards)
        self.game.view_signal.connect(lambda : self.game.view_box(view_deck))
        self.game.empty_signal.connect(self.game.empty_box)
        self.lobby.close()
        self.game.show()
        
    def close_(self):
        global connexion
        connexion.shutdown()
        connexion.close()
        self.game.deleteLater()


class Terminal(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        self.lobby_state = True

    def run(self):
        global connexion
        global window
        global hand
        global view_deck

        cmd = [""]

        while cmd[0] != "/shutdown":
            cmd = connexion.recv(4096)
            cmd = cmd.decode()
            print(cmd)
            cmd = cmd.split()

            if cmd[0] == "/start" and self.lobby_state:
                window.lobby.switch_window.emit()
                self.lobby_state = False


            elif cmd[0] == "/draw" and not self.lobby_state:
                content = connexion.recv(4096)
                if content == b"/empty":
                    window.game.empty_signal.emit()
                else:
                    c = pickle.loads(content)
                    hand.append(c)
                    window.game.refresh_cards.emit()

            elif cmd[0] == "/viewb":
                content = connexion.recv(4096)
                if content == b"/empty":
                    window.game.empty_signal.emit()
                else:
                    view_deck = pickle.loads(content)
                    window.game.view_signal.emit()

            else:
                pass
            
            global kill_terminal
            if kill_terminal:
                break
        
        window.game.switch_window.emit()

class ClientUi(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        global window
        global connexion
        global terminal_thread
        global kill_terminal
        import sys
        app = QtWidgets.QApplication(sys.argv)
        window = Controller()
        window.show_lobby()
        sys.exit(app.exec_())
        try:
            connexion.shutdown()
            connexion.close()
        except:
            pass

name = ""
d_name = ""
ip = ""
port = 0
connexion = None
terminal_thread = None
hand = Deck()
view_deck = Deck()
window = None
kill_terminal = False

client_thread = ClientUi()
client_thread.start()
