import sqlite3
import sys

from ui.rc.app_rc import *
from ui.rc.logout_rc import *
from ui.rc.payment_rc import *

from functools import partial

from auth import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QDialog
from PyQt5.QtCore import Qt, QPropertyAnimation, QRegExp
from PyQt5.QtGui import QRegExpValidator


class MainAppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.payment = Payment()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.current_user = self
        # Передать сюда в переменную значение value (в self.current_balance)
        self.current_balance = 0

        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
        self.ui.pushButton.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.pushButton_5.clicked.connect(self.logout)
        self.ui.wallet.clicked.connect(self.redirect)

    def redirect(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.wallet_page)

        self.ui.home_2.clicked.connect(self.home_redirect)
        self.ui.pushButton_2.clicked.connect(lambda: self.slideLeftMenu_2())
        self.ui.pushButton_6.clicked.connect(self.logout_2)
        self.ui.pushButton_3.clicked.connect(self.shipping_check)

    def shipping_check(self):
        if (self.ui.textEdit.toPlainText()) and not(self.ui.textEdit.toPlainText().isspace()):
            self.top_up_balance()
        else:
            msg = FillUp()
            msg.exec_()

    def top_up_balance(self):
        self.show_payment()

    def show_payment(self):
        if self.payment.exec():
            self.show()

    def home_redirect(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)

    def display_info(self):
        self.ui.account.setText(f'Account: {self.current_user}')
        self.show()

    def logout(self):
        dialog = LogoutDialog(self)
        dialog.exec()

    def logout_2(self):
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

    def slideLeftMenu_2(self):
        width = self.ui.side_menu_2.width()

        if width == 0:
            new_width = 200
        else:
            new_width = 0

        self.animation = QPropertyAnimation(self.ui.side_menu_2, b"minimumWidth")
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


class FillUp(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/ui/fill_up_address.ui', self)
        self.pushButton.clicked.connect(self.ok)
        self.setWindowFlag(Qt.FramelessWindowHint)

    def ok(self):
        self.close()


class Payment(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui = Ui_Payment()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.payment)

        self.ui.cancel.clicked.connect(self.cancel)
        self.ui.proceed.clicked.connect(self.proceed)

        num_validator = QRegExpValidator(QRegExp(r'[0-9]+'))
        abc_validator = QRegExpValidator(QRegExp(r'^[a-zA-Z]*$'))

        self.ui.card_number.setValidator(num_validator)
        self.ui.card_number.setMaxLength(16)
        self.ui.card_number.setInputMask('0000 0000 0000 0000; ')

        self.ui.month.setValidator(num_validator)
        self.ui.month.setMaxLength(2)

        self.ui.year.setValidator(num_validator)
        self.ui.year.setMaxLength(4)

        self.ui.cvv.setValidator(num_validator)
        self.ui.cvv.setMaxLength(4)

        self.ui.cardholder.setValidator(abc_validator)

    def cancel(self):
        self.accept()

    def proceed(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.amount)

        self.ui.hundred.clicked.connect(partial(self.redirect, '100'))
        self.ui.two_hundred.clicked.connect(partial(self.redirect, '250'))
        self.ui.half_thousand.clicked.connect(partial(self.redirect, '500'))
        self.ui.thousand.clicked.connect(partial(self.redirect, '1000'))
        self.ui.two_half_thousand.clicked.connect(partial(self.redirect, '2500'))
        self.ui.five_thousand.clicked.connect(partial(self.redirect, '5000'))

        self.ui.cancel_2.clicked.connect(self.back)
        self.ui.proceed_2.clicked.connect(self.next)

    def back(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.payment)

    def redirect(self, value):
        self.ui.sum.setText(f'{value} $')
        # value передать в MainWindowApp класс

    def next(self):
        if self.ui.sum.text():
            msg = SuccessfullTransaction()
            msg.exec_()
            self.accept()
            self.ui.stackedWidget.setCurrentWidget(self.ui.payment)


class SuccessfullTransaction(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/ui/success_transaction.ui', self)
        self.pushButton.clicked.connect(self.ok)
        self.setWindowFlag(Qt.FramelessWindowHint)

    def ok(self):
        self.accept()
