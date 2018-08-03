# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cal.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import math

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(537, 255)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 3)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 1, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 2, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 2, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 3, 1, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(Form)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 3, 2, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 4, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 4, 1, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(Form)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 4, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_14 = QtWidgets.QPushButton(Form)
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(Form)
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout.addWidget(self.pushButton_15)
        self.pushButton_13 = QtWidgets.QPushButton(Form)
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout.addWidget(self.pushButton_13)
        self.pushButton_16 = QtWidgets.QPushButton(Form)
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout.addWidget(self.pushButton_16)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "1"))
        self.pushButton_2.setText(_translate("Form", "2"))
        self.pushButton_9.setText(_translate("Form", "3"))
        self.pushButton_3.setText(_translate("Form", "4"))
        self.pushButton_6.setText(_translate("Form", "5"))
        self.pushButton_10.setText(_translate("Form", "6"))
        self.pushButton_4.setText(_translate("Form", "7"))
        self.pushButton_7.setText(_translate("Form", "8"))
        self.pushButton_11.setText(_translate("Form", "9"))
        self.pushButton_5.setText(_translate("Form", "0"))
        self.pushButton_8.setText(_translate("Form", "="))
        self.pushButton_12.setText(_translate("Form", "C"))
        self.pushButton_14.setText(_translate("Form", "+"))
        self.pushButton_15.setText(_translate("Form", "-"))
        self.pushButton_13.setText(_translate("Form", "*"))
        self.pushButton_16.setText(_translate("Form", "/"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

