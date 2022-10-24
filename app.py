import sys

from ui.app_rc import *
from ui.logout_rc import *
from auth import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QDialog
from PyQt5.QtCore import Qt, QPropertyAnimation


class MainAppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.current_user = ''

        self.ui.pushButton.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.pushButton_5.clicked.connect(self.logout)

    def logout(self):
        dialog = LogoutDialog(self)
        dialog.exec()

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


class LogoutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.yes_btn.clicked.connect(self.app_quit)
        self.ui.no_btn.clicked.connect(self.app_stay)

    def app_quit(self):
        app = MainAppWindow()
        app.quit()
        self.close()

    def app_stay(self):
        self.close()
