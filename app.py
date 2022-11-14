import sqlite3
import sys

from ui.rc.app_rc import *
from ui.rc.logout_rc import *
from ui.rc.payment_rc import *
from ui.rc.buying_rc import *

from functools import partial

from auth import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QDialog, QButtonGroup
from PyQt5.QtCore import Qt, QPropertyAnimation, QRegExp
from PyQt5.QtGui import QRegExpValidator


class Payment(QDialog):
    submitClicked = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui = Ui_Payment()

        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.payment)

        self.ui.cancel.clicked.connect(self.cancel)
        self.ui.proceed.clicked.connect(self.proceed)

        num_validator = QRegExpValidator(QRegExp(r'[0-9]+'))

        self.ui.card_number.setValidator(num_validator)
        self.ui.card_number.setMaxLength(16)
        self.ui.card_number.setInputMask('0000 0000 0000 0000')

        self.ui.month.setValidator(num_validator)
        self.ui.month.setMaxLength(2)

        self.ui.year.setValidator(num_validator)
        self.ui.year.setMaxLength(4)

        self.ui.cvv.setValidator(num_validator)
        self.ui.cvv.setMaxLength(4)

    def cancel(self):
        self.accept()

    def proceed(self):
        self.ui.error.setText('')
        self.ui.stackedWidget.setCurrentWidget(self.ui.amount)
        self._subwindow = None

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
        self.balance = value

    def next(self):
        if self.ui.sum.text():
            if self._subwindow is None:
                self.submitClicked.emit(self.balance)
                self._subwindow = SuccessfullTransaction()
            self._subwindow.show()
            self._subwindow.activateWindow()
            self.close()
            self.ui.stackedWidget.setCurrentWidget(self.ui.payment)


class BuyingPage(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Buying()
        self.ui.setupUi(self)
        self.app = MainAppWindow()
        self.product = 0
        self.total = 0
        self.balance = 0
        self.remaining = 0
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.ui.proceed.clicked.connect(self.confirmation)
        self.ui.back.clicked.connect(self.back)

    def display_info(self):
        if self.product == 1:
            self.ui.product_name.setText(self.app.ui.buy1text.text())
            self.ui.product_amount.valueChanged.connect(self.update_total)
        if self.product == 2:
            self.ui.product_name.setText(self.app.ui.buy2text.text())
            self.ui.product_amount.valueChanged.connect(self.update_total)

    def update_total(self):
        if self.product == 1:
            self.total = int(self.app.ui.label.text()[:-1]) * int(self.ui.product_amount.text())
            self.ui.total_sum.setText(f'TOTAL: {self.total} $')
        if self.product == 2:
            self.total = int(self.app.ui.label2.text()[:-1]) * int(self.ui.product_amount.text())
            self.ui.total_sum.setText(f'TOTAL: {self.total} $')

    def confirmation(self):
        if self.total > 0:
            self.ui.stackedWidget.setCurrentWidget(self.ui.confirmation_page)
            self.ui.cancel_2.clicked.connect(self.back_2)
            self.ui.balance.setText(f'{self.balance} $')
            self.ui.cart.setText(f'{self.total} $')
            self.remaining = self.balance - self.total
            if self.remaining > 0:
                self.ui.remain.setText(f'{self.remaining} $')

    def back(self):
        self.ui.product_amount.setValue(0)
        self.close()

    def back_2(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.cart_page)


class MainAppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.current_user = False
        self._logout = None
        self._buying = None

        self.is_checked = self

        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
        self.ui.pushButton.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.pushButton_5.clicked.connect(self.logout)
        self.ui.wallet.clicked.connect(self.redirect)

        self.ui.buy1.clicked.connect(partial(self.cart, 1))
        self.ui.buy2.clicked.connect(partial(self.cart, 2))
        self.ui.buy3.clicked.connect(partial(self.cart, 3))
        self.ui.buy4.clicked.connect(partial(self.cart, 4))
        self.ui.buy5.clicked.connect(partial(self.cart, 5))
        self.ui.buy6.clicked.connect(partial(self.cart, 6))

    def set_balance(self):
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute(f'SELECT balance FROM users WHERE login like "{self.current_user}"')
        result = cursor.fetchall()[0][0]
        self.current_balance = result
        self.ui.balance.setText(f'Balance: {self.current_balance} $')

    def redirect(self):
        self._logout_2 = None
        self._shipping = None
        self._payment = None
        self.set_balance()

        self.ui.stackedWidget.setCurrentWidget(self.ui.wallet_page)

        self.ui.home_2.clicked.connect(self.home_redirect)
        self.ui.pushButton_2.clicked.connect(lambda: self.slideLeftMenu_2())
        self.ui.pushButton_6.clicked.connect(self.logout_2)
        self.ui.pushButton_3.clicked.connect(self.shipping_check)

    def shipping_check(self):
        if (self.ui.textEdit.toPlainText()) and not(self.ui.textEdit.toPlainText().isspace()):
            self.top_up_balance()
        else:
            self.appear_warning()

    def appear_warning(self):
        if self._shipping is None:
            self._shipping = FillUp()
        self._shipping.show()
        self._shipping.activateWindow()

    def top_up_balance(self):
        if self._payment is None:
            self._payment = Payment()
            self._payment.submitClicked.connect(self.update_balance)
        self._payment.show()
        self._payment.activateWindow()

    def update_balance(self, balance):
        self.current_balance += int(balance)
        self.ui.balance.setText(f'Balance: {self.current_balance} $')
        db = sqlite3.connect('database.db')
        cursor = db.cursor()

        cursor.execute(f'UPDATE users SET balance={self.current_balance} WHERE login="{self.current_user}"')
        db.commit()

    def home_redirect(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)

    def display_info(self):
        self.ui.account.setText(f'Account: {self.current_user}')
        self.show()

    def cart(self, value):
        self.set_balance()
        if self._buying is None:
            self._buying = BuyingPage()
        self._buying.product = value
        self._buying.display_info()
        self._buying.balance = self.current_balance
        self._buying.show()
        self._buying.activateWindow()

    def logout(self):
        if self._logout is None:
            self._logout = LogoutDialog(self)
        self._logout.show()
        self._logout.activateWindow()

    def logout_2(self):
        if self._logout_2 is None:
            self._logout_2 = LogoutDialog(self)
        self._logout_2.show()
        self._logout_2.activateWindow()

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


class SuccessfullTransaction(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/ui/success_transaction.ui', self)
        self.pushButton.clicked.connect(self.ok)
        self.setWindowFlag(Qt.FramelessWindowHint)

    def ok(self):
        self.close()
