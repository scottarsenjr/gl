# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\pyqt\ui\reg.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import ui.resources.icon_rc


class Ui_RegWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(396, 579)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(9, 22, 41, 255), stop:1 rgba(9, 31, 63, 255))")
        MainWindow.setWindowFilePath("")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-20, -20, 821, 91))
        self.widget.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(5, 13, 25, 255), stop:1 rgba(8, 27, 54, 255))\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 30, 51, 51))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("background-color:\n"
"rgba(255, 255, 255, 0)")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("F:\\pyqt\\ui\\resources/gl3.png"))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 170, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: rgb(255, 255, 255)")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 260, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("color: white;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.reg_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reg_btn.setGeometry(QtCore.QRect(130, 510, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.reg_btn.setFont(font)
        self.reg_btn.setStyleSheet("color: rgb(255, 255, 255)")
        self.reg_btn.setObjectName("reg_btn")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: white;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 230, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: white;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 70, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: white;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 350, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("color: white;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 320, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: white;")
        self.label_5.setObjectName("label_5")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(30, 410, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setUnderline(True)
        self.checkBox.setFont(font)
        self.checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: white;")
        self.checkBox.setText("")
        self.checkBox.setIconSize(QtCore.QSize(32, 32))
        self.checkBox.setChecked(False)
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 420, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: white;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.acc_used = QtWidgets.QLabel(self.centralwidget)
        self.acc_used.setGeometry(QtCore.QRect(0, 460, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.acc_used.setFont(font)
        self.acc_used.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: red;")
        self.acc_used.setText("")
        self.acc_used.setAlignment(QtCore.Qt.AlignCenter)
        self.acc_used.setObjectName("acc_used")
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(10, 80, 31, 41))
        self.back_btn.setStyleSheet("background-color: rgba(255, 255, 255, 0)")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/arrow-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_btn.setIcon(icon)
        self.back_btn.setIconSize(QtCore.QSize(32, 32))
        self.back_btn.setObjectName("back_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GL Launcher"))
        self.reg_btn.setText(_translate("MainWindow", "Register"))
        self.label_2.setText(_translate("MainWindow", "login:"))
        self.label_3.setText(_translate("MainWindow", "password:"))
        self.label_4.setText(_translate("MainWindow", "Registration"))
        self.label_5.setText(_translate("MainWindow", "password (again):"))
        self.label_6.setText(_translate("MainWindow", "I agree with the terms of use"))