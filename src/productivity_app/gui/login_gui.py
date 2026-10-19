from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox
)

from productivity_app.services.login_verification import check_user

WIDTH, HEIGHT = 800, 600

class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(300,300)
        self.setWindowTitle("Register")
        self.email = QLineEdit(placeholderText="Email")
        self.password = QLineEdit(placeholderText="Password")
        
        button = QPushButton("create account")
        button.clicked.connect(self.register_account)

    def register_account(self):
            pass

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MAKE IT ALL")
        self.resize(WIDTH, HEIGHT)

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
        if role == "admin":
            QMessageBox.information(self,"Admin Screen","You are now on the admin screen")
        elif role == "team_member":
            QMessageBox.information(self,"Team member","You are now on the team member screen")
        else:
            QMessageBox.warning(self,"Login fail","Wrong username/password")
            self.password.clear()

    def register(self):
        self.register = RegisterWindow()
        self.register.show()
