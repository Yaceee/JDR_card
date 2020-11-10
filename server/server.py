# coding: utf-8

import random
import socket
import select
import pickle
from threading import Thread
import numpy

element_dict = {
    0: 'Arcane',
    1: 'Feu',
    2: 'Eau',
    3: 'Air',
    4: 'Chaos'
}


### Class des cartes et des joueurs ###

class Carte:
    def __init__(self, e, n): # Carte avec e élement et n nombre
        self.element = e
        self.nombre = n
        self.delete = False
        self.shown = False

    def __repr__(self):
        return element_dict[self.element] + " " + str(self.nombre)

class Deck: # Deck assemblage de carte
    def __init__(self, ls=[], t=""):
        self.deck = ls
        self.tag = t

    def setDeck(self, ls):
        self.deck = ls

    def append(self, c):
        self.deck.append(c)
    
    def pop(self, i=-1):
        return self.deck.pop(i)

    def shuffle(self):
        random.shuffle(self.deck)

    def show(self, n):
        return Deck([self.deck[-i] for i in range(1, min(len(self.deck), n)+1)])

    def __repr__(self):
        chaine = ""
        for c in self.deck:
            chaine += "     {}\n".format(str(c))
        return chaine


class user: # Joueurs : nom, deck, statut admin
    def __init__(self, nom, od=Deck(), a=False):
        self.name = nom
        self.admin = a
        self.own_deck = od
        self.hand = Deck([], "hand")

    def drawown(self):
        self.hand.append(self.own_deck.pop())
        return self.hand.deck[-1]

    def __repr__(self):
        return "Joueur : {}".format(self.name) + "\n Admin : {}".format(str(self.admin)) + "\n Main :\n" + str(self.hand)


### Threads du serveur ###

class Terminal(Thread): # Terminal de commande 
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        global start_serv
        global lobby
        global env
        global players

        while start_serv:
            command = input("> ")
            if command == "shutdown":
                print("Fermeture du serveur")
                start_serv = False
                lobby = False

            elif command == "start":
                lobby = False

            elif command == "stop":
                lobby = True

            elif command == "save":
                with open("jdr.sav", "wb") as file:
                    save = pickle.Pickler(file)
                    save_file =[players, env]
                    save.dump(save_file)
                    print("Partie sauvegardée")

            elif command == "load":
                if lobby:
                    with open("jdr.sav", "rb") as file:
                        save = pickle.Unpickler(file)
                        save_file = save.load()
                        players = save_file[0]
                        env = save_file[1]
                        print("Chargement réussi")
                else:
                    print("Chargement possible que dans le lobby")

            elif command == "nenv":
                with open("env.txt", "r") as f:
                    env = make_deck(deck_decode(f.read()))
                    print("Environnement chargé")

            elif command == "players":
                for p in players:
                    print(p)

            elif command == "connected_players":
                for i in players_dict.values():
                    print(players[i])

            elif command == "setadmin":
                name = input("Nom : ")
                if name != "":
                    try:
                        players[players_dict[name]].admin = True
                        print("Le joueur {} est maintenant administrateur".format(name))
                    except:
                        print("Le joueur n'a pas été trouvé")
                
            elif command == "shuffle_env":
                env.shuffle()

            elif command == "delete_player":
                name = input("Nom du joueur : ")
                conf = input("Etes vous sur ? [Y/N] : ")
                if conf == "Y":
                    n = len(players)
                    for i in range(len(players)):
                        if players[i].name == name:
                            players.pop(i)
                            break
                    if n == len(players):
                        print("Joueur non trouvé")
                    else:
                        print("Le joueur {} a été supprimé".format(name))

            elif command == "show_env":
                print(make_numpy(env))

            elif command == "":
                pass

            else:
                print('Commande non reconnue')

class serv(Thread): # Connexions serveur client 
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        global start_serv
        global lobby

        while start_serv:
            print("-----Lobby-----")
            while lobby:    
                waiting_co, wlist, xlist = select.select([server], [], [], 0.05)
                for co in waiting_co:
                    connected_client.append(co.accept()[0])

                reading = []
                try:
                    reading, wlist, xlist = select.select(connected_client, [], [], 0.05)
                except select.error:
                    pass
                
                else:
                    for client in reading:
                        msg = client.recv(2048)
                        msg = msg.decode()
                        client_cmd(msg, client)
            
            for c in connected_client:
                c.send(b"/start")
            print("Fermeture du lobby")

            while not lobby and start_serv:
                try:
                    reading, wlist, xlist = select.select(connected_client, [], [], 0.05)
                except select.error:
                    pass
            
                else:
                    for client in reading:
                        try:
                            msg = client.recv(2048)
                            msg = msg.decode()
                            client_cmd(msg, client)
                        except:
                            pass

        for c in connected_client:
            c.send(b"/shutdown")


### Fonctions ###

def deck_encode(d): #Conversion de deck numpy => str
    dstr = ""
    for i in range(d.shape()[0]):
        for j in range(d.shape()[1]):
            dstr += "{};".format(str(d[i,j]))
    return dstr

def deck_decode(dstr):#Conversion de deck str => numpy
    dstr = dstr.split(";") + [0,0]
    n = [ [int(dstr[i]), int(dstr[i+1]), int(dstr[i+2])] for i in range(0,len(dstr), 3)]
    n = numpy.array(n)
    return n

def make_deck(n, t=""):#Conversion numpy => deck
    d = Deck([], t)
    for i in range(n.shape[0]):
        for j in range(n.shape[1]):
            for k in range(n[i,j]):
                d.append(Carte(i,j+1))
    return d

def make_numpy(d):#Conversion deck => numpy
    n = numpy.zeros((5,3))
    for c in d.deck:
        n[c.element, c.nombre - 1] += 1
    return n


def client_cmd(cmd, client):  #Lecture des commande client
    global start_serv
    global lobby
    global players
    global env
    global players_dict

    cmd = cmd.split()

    if cmd[0] == "/shutdown":#Arret
        start_serv = False
        lobby = False

    elif cmd[0] == "/ping":#Ping
        client.send(b"ping")

    elif cmd[0] == "/save":#Sauvegarde
        with open("jdr.sav", "wb") as file:
            save = pickle.Pickler(file)
            save_file =[players, env]
            save.dump(save_file)
            client.send(b"Partie sauvegardee")

    elif cmd[0] == "/load":#Chargement
        if lobby:
            with open("jdr.sav", "rb") as file:
                save = pickle.Unpickler(file)
                save_file = save.load()
                players = save_file[0]
                env = save_file[1]
                client.send(b"Chargement reussi")
        else:
            client.send(b"Chargement possible uniquement dans le lobby")

    elif cmd[0] == "/connect":#Connexion d'un joueur
        try:
            new = True
            for i in range(len(players)):
                p = players[i]
                if p.name == cmd[1]:
                    players_dict[cmd[1]] = i
                    client.send(b"load profile")
                    client.send(pickle.dumps(p.hand))
                    print("Joueur connecté : {}".format(cmd[1]))
                    new = False
                    break
            
            if new:
                players_dict[cmd[1]] = len(players)
                if len(cmd) == 2:
                    players.append(user(cmd[1]))
                elif len(cmd) == 3:
                    own_deck = make_deck(deck_decode(cmd[2]), "own_deck")
                    players.append(user(cmd[1], own_deck))
                    players[-1].own_deck.shuffle()
                elif len(cmd) == 4 and cmd[3] == "a":
                    own_deck = make_deck(deck_decode(cmd[2]), "own_deck")
                    players.append(user(cmd[1], own_deck, True))
                    players[-1].own_deck.shuffle()
                print("Nouveau joueur : {}".format(cmd[1]))
                
                client.send(b"new profile")
        except:
            pass

    elif cmd[0] == "/shuffle":#Melange de deck
        if cmd[1] == "env":
            random.shuffle(env.deck)
        else:
            random.shuffle(players[players_dict[cmd[1]]].own_deck.deck)
        client.send(b"ok")


    elif cmd[0] == "/draw":#Joueur pioche une carte
        i = players_dict[cmd[1]]
        client.send(b"/draw")
        try:
            if cmd[2] == "own":
                c = players[i].own_deck.deck.pop()
                players[i].hand.deck.append(c)
                print(make_numpy(players[i].own_deck))
                client.send(pickle.dumps(c))
            elif cmd[2] == "env":
                p = players[i]
                p.hand.append(env.deck.pop())
                players[i] = p
                client.send(pickle.dumps(p.hand.deck[-1]))
        except IndexError:
            print("empty")
            client.send(b"/empty")


    
    elif cmd[0] == "/discard":
        i = players_dict[cmd[1]]
        env.deck = [players[i].hand.deck.pop(int(cmd[2]))] + env.deck

    elif cmd[0] == "/view":
        client.send(b"/viewb")
        try:            
            if cmd[2] == "env":
                client.send(pickle.dumps(env.show(int(cmd[3]))))
            elif cmd[2] == "own":
                client.send(pickle.dumps(players[players_dict[cmd[1]]].hand.show(int(cmd[3]))))
        except:
            client.send(b"/empty")

    else:
        client.send(b"Commande non reconnue")
    

  

### script principal ###
start_serv = True
lobby = True
port = 1570
host = ''
connected_client = []
players = []
players_dict = dict()
env = Deck([], "env")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)
print("Serveur lancé sur le port {}".format(port))

thread_1 = serv()
thread_2 = Terminal()

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()
