#from src.productivity_app.services.login_verification import check_user


from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox
)
import string
from productivity_app.services.login_verification import check_user

WIDTH, HEIGHT = 300, 300

class RegisterWindow(QWidget):
    def __init__(self,on_back):
        super().__init__()
        self.on_back = on_back

        self.resize(300,300)
        self.setWindowTitle("Register")
        self.email = QLineEdit(placeholderText="Email")
        self.password = QLineEdit(placeholderText="Password")
        
        button = QPushButton("create account")
        button.clicked.connect(self.register_account)

        back_button = QPushButton("Back to login")
        back_button.clicked.connect(self.go_back)

        layout = QVBoxLayout(self)

        layout.addWidget(self.email)
        layout.addWidget(self.password)
        layout.addWidget(button)
        layout.addWidget(back_button)

    def go_back(self):
        #window = LoginWindow()
        #window.show()
        #self.login_window.show()
        #self.close()
        self.on_back()


    def register_account(self):
            email = self.email.text().strip()
            password = self.password.text()
            error = self.check_valid_password(password)

    def check_valid_password(self,password):
        if len(password) < 8:
            print("password needs to be atleast 8 character long")
        lower =  any(c.islower() for c in password)
        upper = any(c.upper() for c in password)
        special = any(c in string.punctuation for c in password)
        digit = any(c.isdigit() for c in password)
        if not lower:
            print("password must contain a lower case character")
        if not upper:
            print("password must contain an upper case character")
        if not special:
            print("password must contain a special character")
        if not digit:
            print("password must contain a digit ")
        


class LoginWindow(QWidget):
    def __init__(self, verify_login, on_register):
        super().__init__()

        self.verify_login = verify_login
        self.setWindowTitle("MAKE IT ALL")
        self.resize(WIDTH, HEIGHT)
        self.on_register = on_register

        self.username = QLineEdit(placeholderText="Username")
        self.password = QLineEdit(placeholderText="Password", echoMode=QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)

        self.register_button = QPushButton("Register")
        self.register_button.clicked.connect(self.register)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("LOGIN MENU"))
        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)

    def login(self):
        role = check_user(self.username.text(),self.password.text())
        if role == "team_leader":
            QMessageBox.information(self,"Team Leader Screen","You are now on the team leader screen")
        elif role == "team_member":
            QMessageBox.information(self,"Team member","You are now on the team member screen")
        else:
            QMessageBox.warning(self,"Login fail","Wrong username/password")
            self.password.clear()

    def register(self):
        #self.register = RegisterWindow()
        #self.register.show()
        self.on_register()
