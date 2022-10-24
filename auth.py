import random, sqlite3, sys, time

from PyQt5 import uic
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from app import *
from ui.reg_rc import *

db = sqlite3.connect('database.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users(
    login TEXT,
    password TEXT
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

        uic.loadUi('ui/main.ui', self)

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


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.auth = {}
        self.app_redirect = MainAppWindow()
        self.register_redirect = RegisterWindow()

        self.setWindowFlag(Qt.FramelessWindowHint)

        uic.loadUi('ui/auth.ui', self)

        self.pushButton.pressed.connect(self.login)
        self.pushButton_2.pressed.connect(self.register)

    def login(self):
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()

        for j, k in result:
            self.auth[j] = k

        if self.lineEdit.text() in self.auth:
            if self.lineEdit_2.text() == self.auth.get(self.lineEdit.text()):
                self.close()
                self.app_redirect.show()
            else:
                self.Incorrect.setText('Wrong login or password')
        else:
            self.Incorrect.setText('Wrong login or password')

    def register(self):
        self.hide()
        self.register_redirect.show()


class RegisterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.app_redirect = MainAppWindow()
        self.ui = Ui_RegWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)

        self.ui.reg_btn.clicked.connect(self.register)

    def register(self):
        user_login = self.ui.lineEdit.text()
        user_password = self.ui.lineEdit_2.text()

        if len(user_login) == 0:
            return

        if len(user_password) == 0:
            return

        cursor.execute(f'SELECT login FROM users WHERE login="{user_login}"')
        if cursor.fetchone() is None:
            if self.ui.lineEdit_2.text() == self.ui.lineEdit_3.text():
                if self.ui.checkBox.isChecked():
                    cursor.execute(f'INSERT INTO users VALUES ("{user_login}", "{user_password}")')
                    self.close()
                    self.app_redirect.show()
                    db.commit()
                else:
                    self.ui.acc_used.setText('You must to agree to the terms of use.')
            else:
                self.ui.acc_used.setText('Passwords are not the same.')
        else:
            self.ui.acc_used.setText(f'Account {user_login} is already in use.')


def window():
    app = QtWidgets.QApplication(sys.argv)
    lgn = LoginWindow()
    reg = RegisterWindow()
    main = ConnectWindow()
    lgn.pushButton_2.clicked.connect(reg.show)
    lgn.pushButton_2.clicked.connect(lgn.close)
    reg.ui.back_btn.clicked.connect(lgn.show)
    reg.ui.back_btn.clicked.connect(reg.close)
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
