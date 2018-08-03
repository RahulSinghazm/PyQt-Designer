# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WindowTitle(object):
    def setupUi(self, WindowTitle):
        WindowTitle.setObjectName("WindowTitle")
        WindowTitle.resize(500, 500)
        self.centralwidget = QtWidgets.QWidget(WindowTitle)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 260, 91, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 70, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 260, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 70, 161, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 260, 171, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 70, 91, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.WindowTitle_2 = QtWidgets.QLabel(self.centralwidget)
        self.WindowTitle_2.setGeometry(QtCore.QRect(80, 110, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.WindowTitle_2.setFont(font)
        self.WindowTitle_2.setObjectName("WindowTitle_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 310, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        WindowTitle.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WindowTitle)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        WindowTitle.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WindowTitle)
        self.statusbar.setObjectName("statusbar")
        WindowTitle.setStatusBar(self.statusbar)

        self.retranslateUi(WindowTitle)
        QtCore.QMetaObject.connectSlotsByName(WindowTitle)

    def retranslateUi(self, WindowTitle):
        _translate = QtCore.QCoreApplication.translate
        WindowTitle.setWindowTitle(_translate("WindowTitle", "MainWindow"))
        self.pushButton_2.setText(_translate("WindowTitle", "Find Total"))
        self.label.setText(_translate("WindowTitle", "Book Title:"))
        self.label_2.setText(_translate("WindowTitle", "Quantity:"))
        self.pushButton.setText(_translate("WindowTitle", "Find Price"))
        self.WindowTitle_2.setText(_translate("WindowTitle", "Price:"))
        self.label_4.setText(_translate("WindowTitle", "Total:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowTitle = QtWidgets.QMainWindow()
    ui = Ui_WindowTitle()
    ui.setupUi(WindowTitle)
    WindowTitle.show()
    sys.exit(app.exec_())

