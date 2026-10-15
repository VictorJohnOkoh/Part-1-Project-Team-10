from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
)

from productivity_app.services.login_verification import check_user, check_password

WIDTH, HEIGHT = 800, 600

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MAKE IT ALL")
        self.resize(WIDTH, HEIGHT)

        self.username = QLineEdit(placeholderText="Username")
        self.password = QLineEdit(placeholderText="Password", echoMode=QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("LOGIN MENU"))
        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(self.login_button)

    def login(self):
        if check_user(self.username.text()):
            print("User exists")
        else:
            print("User does not exist")
        if check_password(self.password.text()):
            print("Password correct")
        else:
            print("Password incorrect")