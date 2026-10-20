from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton, QMessageBox,
)

from productivity_app.services.login_verification import LoginVerification
from productivity_app.services import check_user, check_password

WIDTH, HEIGHT = 800, 600

class LoginWindow(QWidget):
    def __init__(self, verify_login):
        super().__init__()

        self.verify_login = verify_login
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
        if check_user(self.username.text()) == LoginVerification.MANAGER and check_password(self.password.text()) == LoginVerification.MANAGER:
            self.verify_login()
        elif check_password(self.password.text()) and check_user(self.username.text()):
            return "employee"
        else:
<<<<<<< HEAD
            self.show_error()
            return None

    def show_error(self):
        QMessageBox.warning(self, "Error", "Invalid username or password")


=======
            print("User does not exist")
        if check_password(self.password.text()):
            print("Password correct")
        else:
            print("Password incorrect")

if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
>>>>>>> 140813e (Changed toml and updated login gui to view system gui)
