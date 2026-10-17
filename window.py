import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel,QPushButton,
    QLineEdit,QVBoxLayout,QGridLayout,
    QMessageBox
    
    )
import re
import string
# Notes: implement the login system using password industry standard
# add a register option. 
# email checking
# 

class dashboard_window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600,300)
        self.setWindowTitle("Dashboard")
#this class is for the window where the users can enter their login details to enter the system

class register_window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300,300)
        self.setWindowTitle("Register")
        self.email = QLineEdit(placeholderText="Email")
        self.password = QLineEdit(placeholderText="Password")

        button = QPushButton("create account")
        button.clicked.connect(self.register)

        layout = QVBoxLayout(self)

        layout.addWidget(self.email)
        layout.addWidget(self.password)
        layout.addWidget(button)

    def register(self):
        email = self.email.text().strip()
        password = self.password.text()

        error = self.check_password(password)
        if error:
            QMessageBox.warning(self, "Password too weak",error)
            return

    def check_password(self, password):
        #special_character = "!@#$%^&*()-=_+[]{}|:;'\",.<>/?"
        if len(password) < 12:
            print("password must be atleast 12 character long")
        #if re.search(r)
        lower =  any(c.islower() for c in password)
        upper = any(c.upper() for c in password)
        special = any(c in string.punctuation for c in password)
        digit = any(c.isdigit() for c in password)
    
        if not (lower and upper and special and digit):
            print("password must contain lower case upper case special and digit")
        return None

class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.resize(300,300)
        self.setWindowTitle("Make It All ")
        self.username = QLineEdit(placeholderText="Username")
        self.password = QLineEdit(placeholderText="Password")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        button = QPushButton("Login")
        button.clicked.connect(self.login)

        register_button = QPushButton("Register")
        register_button.clicked.connect(self.register)

        layout = QVBoxLayout(self)
        #layout.addWidget(title)
        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(button)
        layout.addWidget(register_button)

    def register(self):
        self.register = register_window()
        self.register.show()

    def check_password(self, password):
        #special_character = "!@#$%^&*()-=_+[]{}|:;'\",.<>/?"
        if len(password) < 12:
            print("password must be atleast 12 character long")
        #if re.search(r)
        lower =  any(c.islower() for c in password)
        upper = any(c.upper() for c in password)
        special = any(c in string.punctuation for c in password)
        digit = any(c.isdigit() for c in password)

        if not (lower or upper or special or digit):
            print("password must contain lower case upper case special and digit")
        return None

    #this function is where the checks are ran to make sure the user is authorised
    def login(self):
        if self.username.text() == "a" and self.password.text() == "a":
            self.dashboard_window = dashboard_window()
            self.dashboard_window.show()
            self.close()
        else:
            QMessageBox.warning(self,"Login fail","Wrong username/password")
            self.password.clear()




app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec())