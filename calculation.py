# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculation.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import math

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.t1 = QtWidgets.QLineEdit(self.centralwidget)
        self.t1.setGeometry(QtCore.QRect(220, 180, 113, 20))
        self.t1.setObjectName("t1")
        self.t2 = QtWidgets.QLineEdit(self.centralwidget)
        self.t2.setGeometry(QtCore.QRect(220, 240, 113, 20))
        self.t2.setObjectName("t2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 180, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 240, 91, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuVies = QtWidgets.QMenu(self.menubar)
        self.menuVies.setObjectName("menuVies")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionsqure = QtWidgets.QAction(MainWindow)
        self.actionsqure.setShortcut("")
        self.actionsqure.setObjectName("actionsqure")
        self.actionroot = QtWidgets.QAction(MainWindow)
        self.actionroot.setObjectName("actionroot")
        self.actioncube = QtWidgets.QAction(MainWindow)
        self.actioncube.setObjectName("actioncube")
        self.actioncuberoot = QtWidgets.QAction(MainWindow)
        self.actioncuberoot.setObjectName("actioncuberoot")
        self.actioncubesqr = QtWidgets.QAction(MainWindow)
        self.actioncubesqr.setObjectName("actioncubesqr")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionSquare = QtWidgets.QAction(MainWindow)
        self.actionSquare.setObjectName("actionSquare")
        self.actionCubeRoot = QtWidgets.QAction(MainWindow)
        self.actionCubeRoot.setObjectName("actionCubeRoot")
        self.actionCube = QtWidgets.QAction(MainWindow)
        self.actionCube.setObjectName("actionCube")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSquare)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionCubeRoot)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionCube)
        self.menuVies.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuVies.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.menuFile.triggered[QtWidgets.QAction].connect(self.menufunction)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Number"))
        self.label_2.setText(_translate("MainWindow", "Result"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuVies.setTitle(_translate("MainWindow", "Vies"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionsqure.setText(_translate("MainWindow", "squre"))
        self.actionroot.setText(_translate("MainWindow", "root"))
        self.actioncube.setText(_translate("MainWindow", "cube"))
        self.actioncuberoot.setText(_translate("MainWindow", "cuberoot"))
        self.actioncubesqr.setText(_translate("MainWindow", "cubesqr"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionSquare.setText(_translate("MainWindow", "Square"))
        self.actionCubeRoot.setText(_translate("MainWindow", "CubeRoot"))
        self.actionCube.setText(_translate("MainWindow", "Cube"))

    def menufunction(self, action):
        txt= (action.text())
        no=int(self.t1.text())
        print (txt, no)
        if txt =='Square':
            self.t2.setText(str(no*no))
        if txt =='Cube':
            self.t2.setText(str(no*no*no))
        if txt =='SqrRoot':
            self.t2.setText(str(math.sqrt(no)))
        if txt=='CubeRoot':
            self.t2.setText(str(math.pow(no,1/3)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

