from PyQt5 import QtCore, QtGui, QtWidgets
import ui.resources.icon_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(994, 613)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("*{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    color: #fff;\n"
"}\n"
"#centralwiget{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"#side_menu{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(9, 22, 41, 255), stop:1 rgba(9, 31, 63, 255));\n"
"    border-radius: 20px;\n"
"}\n"
"#header{\n"
"    background-color: rgb(5, 17, 34);\n"
"}\n"
"QPushButton{\n"
"    padding: 10px;\n"
"    background-color: rgb(5, 17, 34);\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.130682, y2:0.165, stop:0 rgba(34, 120, 239, 255), stop:1 rgba(145, 185, 239, 255));\n"
"}\n"
"#main_body{\n"
"    background-color: white;\n"
"    border-radius: 10px;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.header.setMinimumSize(QtCore.QSize(0, 0))
        self.header.setMaximumSize(QtCore.QSize(16777215, 100))
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.side_menu_toggle = QtWidgets.QFrame(self.header)
        self.side_menu_toggle.setMinimumSize(QtCore.QSize(100, 0))
        self.side_menu_toggle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.side_menu_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_menu_toggle.setObjectName("side_menu_toggle")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.side_menu_toggle)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.side_menu_toggle)
        self.pushButton.setMinimumSize(QtCore.QSize(170, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(170, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: white;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/align-justify.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/align-justify.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(24, 24))
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.horizontalLayout_2.addWidget(self.side_menu_toggle, 0, QtCore.Qt.AlignLeft)
        self.frame_3 = QtWidgets.QFrame(self.header)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("F:\\pyqt\\ui\\resources/gl3.png"))
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.header)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 500))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 500))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.side_menu = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.side_menu.sizePolicy().hasHeightForWidth())
        self.side_menu.setSizePolicy(sizePolicy)
        self.side_menu.setMinimumSize(QtCore.QSize(0, 0))
        self.side_menu.setMaximumSize(QtCore.QSize(0, 16777215))
        self.side_menu.setObjectName("side_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.side_menu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.side_menu)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_2.setMinimumSize(QtCore.QSize(170, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(170, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_3.setMinimumSize(QtCore.QSize(170, 53))
        self.pushButton_3.setMaximumSize(QtCore.QSize(170, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.verticalLayout_2.addWidget(self.frame_5, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.frame = QtWidgets.QFrame(self.side_menu)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setMinimumSize(QtCore.QSize(170, 0))
        self.pushButton_5.setMaximumSize(QtCore.QSize(170, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(165, 4, 77, 255), stop:1 rgba(165, 117, 139, 255));\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/log-out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_5.addWidget(self.pushButton_5)
        self.verticalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.horizontalLayout.addWidget(self.side_menu)
        self.main_body = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy)
        self.main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.main_body)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.main_body)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: black;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.horizontalLayout.addWidget(self.main_body)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "MENU"))
        self.pushButton_2.setText(_translate("MainWindow", "HOME"))
        self.pushButton_3.setText(_translate("MainWindow", "PROFILE"))
        self.pushButton_5.setText(_translate("MainWindow", "LOGOUT"))
        self.label_2.setText(_translate("MainWindow", "CONTENT"))
