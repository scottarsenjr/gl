import random, sqlite3, sys, time

from PyQt5 import uic
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QMessageBox
from app import *
from ui.rc.reg_rc import *
from ui.rc.login_rc import *

db = sqlite3.connect('database.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users(
    login TEXT,
    password TEXT,
    balance INTEGER
)''')
db.commit()


class ProgressHandler(QThread):
    mysignal = pyqtSignal(list)

    def run(self):
        for step in range(0, 101):
            self.mysignal.emit(['progress_increment', step])
            time.sleep(0.03)


class ConnectWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.auth = LoginWindow()

        uic.loadUi('ui/ui/main.ui', self)

        self.setWindowTitle('GL Launcher')
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.handler = ProgressHandler()
        self.handler.mysignal.connect(self.signal_handler)
        self.handler.start()

    def signal_handler(self, value):
        fake_data = [
            'Loading resources', 'Clearing cache',
            'Collecting data', 'Connecting to the server'
        ]

        if value[1] == 100:
            time.sleep(1)
            self.auth_redirect()
            return

        if value[0] == 'progress_increment':
            current_value = self.progressBar.value()
            self.progressBar.setValue(current_value + 1)

            if value[1] % 25 == 0:
                random_data = random.choice(fake_data)
                self.label_2.setText(random_data)

    def auth_redirect(self):
        self.hide()
        self.auth.show()


class LoginWindow(QDialog):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.auth = {}
        self.app_redirect = MainAppWindow()
        self.reg = RegisterWindow()
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.ui = Ui_Login()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.login)
        self.ui.pushButton_2.clicked.connect(self.register_redirect)

    def login(self):
        cursor.execute("SELECT login, password FROM users")
        result = cursor.fetchall()

        for j, k in result:
            self.auth[j] = k

        if len(self.ui.lineEdit.text()) == 0:
            return

        if len(self.ui.lineEdit_2.text()) == 0:
            return

        if self.ui.lineEdit.text() in self.auth:
            if self.ui.lineEdit_2.text() == self.auth.get(self.ui.lineEdit.text()):
                self.close()
                self.pass_info()
            else:
                self.ui.Incorrect.setText('Wrong login or password')
        else:
            self.ui.Incorrect.setText('Wrong login or password')

    def register_redirect(self):
        self.hide()
        self.show_reg()

    def show_reg(self):
        if self.reg.exec():
            self.show()

    def pass_info(self):
        self.app_redirect.current_user = self.ui.lineEdit.text()
        self.app_redirect.display_info()


class RegisterWindow(QDialog):
    def __init__(self):
        super(RegisterWindow, self).__init__()
        self.app_redirect = MainAppWindow()
        self.ui = Ui_Registration()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)

        self.ui.reg_btn.clicked.connect(self.register)
        self.ui.back_btn.clicked.connect(self.login_redirect)

    def register(self):
        user_login = self.ui.lineEdit.text()
        user_password = self.ui.lineEdit_2.text()
        balance = 0

        if len(user_login) == 0:
            return

        if len(user_password) == 0:
            return

        cursor.execute(f'SELECT login FROM users WHERE login="{user_login}"')
        if cursor.fetchone() is None:
            if self.ui.lineEdit_2.text() == self.ui.lineEdit_3.text():
                if self.ui.checkBox.isChecked():
                    cursor.execute(f'INSERT INTO users VALUES ("{user_login}", "{user_password}", {balance})')
                    self.close()
                    self.show_success_register()
                    self.login_redirect()
                    db.commit()
                else:
                    self.ui.acc_used.setText('You must to agree to the terms of use.')
            else:
                self.ui.acc_used.setText('Passwords are not the same.')
        else:
            self.ui.acc_used.setText(f'Account {user_login} is already in use.')

    def login_redirect(self):
        self.accept()

    def show_success_register(self):
        msg = SuccessWindow()
        msg.exec_()


class SuccessWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/ui/success_reg.ui', self)
        self.pushButton.clicked.connect(self.ok)
        self.setWindowFlag(Qt.FramelessWindowHint)

    def ok(self):
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = ConnectWindow()
    main.show()
    sys.exit(app.exec_())
