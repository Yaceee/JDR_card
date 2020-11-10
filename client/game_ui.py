# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/test/client_1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1070, 264)
        MainWindow.setFixedSize(1070, 264)
        MainWindow.setWindowTitle("JDR 13")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(180, 10, 861, 231))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 859, 229))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.hbox = QtWidgets.QHBoxLayout()
        self.scrollAreaWidgetContents.setLayout(self.hbox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 11, 157, 234))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.env_groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.env_groupBox.setObjectName("env_groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.env_groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.drawenv_pushButton = QtWidgets.QPushButton(self.env_groupBox)
        self.drawenv_pushButton.setObjectName("drawenv_pushButton")
        self.verticalLayout.addWidget(self.drawenv_pushButton)
        self.seeenv_pushButton = QtWidgets.QPushButton(self.env_groupBox)
        self.seeenv_pushButton.setObjectName("seeenv_pushButton")
        self.verticalLayout.addWidget(self.seeenv_pushButton)
        self.seeenv_spinBox = QtWidgets.QSpinBox(self.env_groupBox)
        self.seeenv_spinBox.setObjectName("seeenv_spinBox")
        self.verticalLayout.addWidget(self.seeenv_spinBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_5.addWidget(self.env_groupBox)
        self.deck_groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.deck_groupBox.setObjectName("deck_groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.deck_groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.drawdeck_pushButton = QtWidgets.QPushButton(self.deck_groupBox)
        self.drawdeck_pushButton.setObjectName("drawdeck_pushButton")
        self.verticalLayout_4.addWidget(self.drawdeck_pushButton)
        self.seedeck_pushButton = QtWidgets.QPushButton(self.deck_groupBox)
        self.seedeck_pushButton.setObjectName("seedeck_pushButton")
        self.verticalLayout_4.addWidget(self.seedeck_pushButton)
        self.seedeck_spinBox = QtWidgets.QSpinBox(self.deck_groupBox)
        self.seedeck_spinBox.setObjectName("seedeck_spinBox")
        self.verticalLayout_4.addWidget(self.seedeck_spinBox)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addWidget(self.deck_groupBox)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "JDR 13"))
        self.env_groupBox.setTitle(_translate("MainWindow", "Environnement"))
        self.drawenv_pushButton.setText(_translate("MainWindow", "Piocher"))
        self.seeenv_pushButton.setText(_translate("MainWindow", "Voir"))
        self.deck_groupBox.setTitle(_translate("MainWindow", "Deck joueur"))
        self.drawdeck_pushButton.setText(_translate("MainWindow", "Piocher"))
        self.seedeck_pushButton.setText(_translate("MainWindow", "Voir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
