import sys

from ui.app_rc import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QDialog
from PyQt5.QtCore import Qt, QPropertyAnimation


class MainAppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.ui.pushButton.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.pushButton_5.clicked.connect(self.logout)

    def logout(self):
        pass

    def slideLeftMenu(self):
        width = self.ui.side_menu.width()

        if width == 0:
            new_width = 200
        else:
            new_width = 0

        self.animation = QPropertyAnimation(self.ui.side_menu, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
