# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\env.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(257,216)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/13.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 211, 179))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.simple_label = QtWidgets.QLabel(self.widget)
        self.simple_label.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.simple_label.setFont(font)
        self.simple_label.setObjectName("simple_label")
        self.gridLayout.addWidget(self.simple_label, 0, 1, 1, 1)
        self.double_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.double_label.setFont(font)
        self.double_label.setObjectName("double_label")
        self.gridLayout.addWidget(self.double_label, 0, 2, 1, 1)
        self.triple_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.triple_label.setFont(font)
        self.triple_label.setObjectName("triple_label")
        self.gridLayout.addWidget(self.triple_label, 0, 3, 1, 1)
        self.arcane_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.arcane_label.setFont(font)
        self.arcane_label.setObjectName("arcane_label")
        self.gridLayout.addWidget(self.arcane_label, 1, 0, 1, 1)
        self.arcane1_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.arcane1_lineEdit.setObjectName("arcane1_lineEdit")
        self.gridLayout.addWidget(self.arcane1_lineEdit, 1, 1, 1, 1)
        self.arcane2_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.arcane2_lineEdit.setObjectName("arcane2_lineEdit")
        self.gridLayout.addWidget(self.arcane2_lineEdit, 1, 2, 1, 1)
        self.arcane3_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.arcane3_lineEdit.setObjectName("arcane3_lineEdit")
        self.gridLayout.addWidget(self.arcane3_lineEdit, 1, 3, 1, 1)
        self.feu_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.feu_label.setFont(font)
        self.feu_label.setObjectName("feu_label")
        self.gridLayout.addWidget(self.feu_label, 2, 0, 1, 1)
        self.feu1_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.feu1_lineEdit.setObjectName("feu1_lineEdit")
        self.gridLayout.addWidget(self.feu1_lineEdit, 2, 1, 1, 1)
        self.feu2_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.feu2_lineEdit.setObjectName("feu2_lineEdit")
        self.gridLayout.addWidget(self.feu2_lineEdit, 2, 2, 1, 1)
        self.feu3_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.feu3_lineEdit.setObjectName("feu3_lineEdit")
        self.gridLayout.addWidget(self.feu3_lineEdit, 2, 3, 1, 1)
        self.eau_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.eau_label.setFont(font)
        self.eau_label.setObjectName("eau_label")
        self.gridLayout.addWidget(self.eau_label, 3, 0, 1, 1)
        self.eau1_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.eau1_lineEdit.setObjectName("eau1_lineEdit")
        self.gridLayout.addWidget(self.eau1_lineEdit, 3, 1, 1, 1)
        self.eau2_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.eau2_lineEdit.setObjectName("eau2_lineEdit")
        self.gridLayout.addWidget(self.eau2_lineEdit, 3, 2, 1, 1)
        self.eau3_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.eau3_lineEdit.setObjectName("eau3_lineEdit")
        self.gridLayout.addWidget(self.eau3_lineEdit, 3, 3, 1, 1)
        self.air_client = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.air_client.setFont(font)
        self.air_client.setObjectName("air_client")
        self.gridLayout.addWidget(self.air_client, 4, 0, 1, 1)
        self.air1_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.air1_lineEdit.setObjectName("air1_lineEdit")
        self.gridLayout.addWidget(self.air1_lineEdit, 4, 1, 1, 1)
        self.air2_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.air2_lineEdit.setObjectName("air2_lineEdit")
        self.gridLayout.addWidget(self.air2_lineEdit, 4, 2, 1, 1)
        self.air3_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.air3_lineEdit.setObjectName("air3_lineEdit")
        self.gridLayout.addWidget(self.air3_lineEdit, 4, 3, 1, 1)
        self.chaos_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chaos_label.setFont(font)
        self.chaos_label.setObjectName("chaos_label")
        self.gridLayout.addWidget(self.chaos_label, 5, 0, 1, 1)
        self.chaos1_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.chaos1_lineEdit.setObjectName("chaos1_lineEdit")
        self.gridLayout.addWidget(self.chaos1_lineEdit, 5, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.create_pushButton = QtWidgets.QPushButton(self.widget)
        self.create_pushButton.setObjectName("create_pushButton")
        self.verticalLayout.addWidget(self.create_pushButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.create_pushButton.clicked.connect(self.create_env)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EnvMaker"))
        self.simple_label.setText(_translate("MainWindow", "Simple"))
        self.double_label.setText(_translate("MainWindow", "Double"))
        self.triple_label.setText(_translate("MainWindow", "Triple"))
        self.arcane_label.setText(_translate("MainWindow", "Arcane"))
        self.feu_label.setText(_translate("MainWindow", "Feu"))
        self.eau_label.setText(_translate("MainWindow", "Eau"))
        self.air_client.setText(_translate("MainWindow", "Air"))
        self.chaos_label.setText(_translate("MainWindow", "Chaos"))
        self.create_pushButton.setText(_translate("MainWindow", "Créer"))

    def create_env(self):
        case = [self.arcane1_lineEdit, self.arcane2_lineEdit, self.arcane3_lineEdit,
        self.feu1_lineEdit, self.feu2_lineEdit, self.feu3_lineEdit,
        self.eau1_lineEdit, self.eau2_lineEdit, self.eau3_lineEdit,
        self.air1_lineEdit, self.air2_lineEdit, self.air3_lineEdit,
        self.chaos1_lineEdit]
        env_str = ""
        try:
            for c in case:
                if c.text() != "":
                    if int(c.text()) > 0:
                        env_str += "{};".format(c.text())
                else:
                    env_str += "0;"
            env_str = env_str[0:-1]
            with open("env.txt", 'w') as f:
                f.write(env_str)
        except:
            alert = QtWidgets.QMessageBox()
            alert.setIcon(QtWidgets.QMessageBox.Critical)
            alert.setWindowTitle("Erreur")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icon\effacer.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
            alert.setWindowIcon(icon)
            alert.setText("Valeurs invalides. \nEntrez uniquement des nombres.")
            alert.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
