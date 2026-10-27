#from src.productivity_app.services.login_verification import check_user


from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox,
)
import string
from productivity_app.services.login_verification import check_user, add_user, get_authorised, user_exist
from PyQt6.QtCore import Qt
import re
WIDTH, HEIGHT = 300, 300
maximum = 5

class RegisterWindow(QWidget):
    def __init__(self,on_back):
        super().__init__()
        self.on_back = on_back

        self.resize(WIDTH, HEIGHT)
        self.setWindowTitle("Register")
        self.email = QLineEdit(placeholderText="Email")
        self.password = QLineEdit(placeholderText="Password",echoMode=QLineEdit.EchoMode.Password)
        
        button = QPushButton("Create Account")
        button.clicked.connect(self.register_account)

        back_button = QPushButton("Back to login")
        back_button.clicked.connect(self.go_back)
        title = QLabel("MAKE-IT-ALL")
        font = title.font()
        font.setBold(True)
        font.setPointSize(22)
        title.setFont(font)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        heading = QLabel("Register")
        heading_font = heading.font()
        heading_font.setBold(True)
        heading_font.setPointSize(16)
        heading.setFont(heading_font)
        heading.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.email.setMinimumHeight(40)
        self.password.setMinimumHeight(40)
        button.setMinimumHeight(40)
        back_button.setMinimumHeight(40)
        

        layout = QVBoxLayout(self)

        #layout.addWidget(QLabel("Register"))
        layout.addStretch()
        layout.addWidget(title)
        layout.addWidget(heading)
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
            self.check_email(email)
            error = self.check_valid_password(password)
            role = get_authorised(email)
            if role is None:
                QMessageBox.warning(self,"Not authorised","this email is not auuthorised")
                return
            if user_exist(email):
                QMessageBox.warning(self,"Account exists", "This account already exists")
                return            
            if error:
                QMessageBox.warning(self,"Password too weak", error)
            #role = get_authorised(email)
            

            add_user(email,password,role)
            QMessageBox.information(self,"success","account created")

 

    def check_email(self, email):
        email = email.lower()
        if not re.search(r"^[^@\s]+@make-it-all\.co\.uk$",email): # one or more character no @ or space efore the @ in the email. 
            QMessageBox.warning(self,"invalide email", "email must be name@make-it-all.co.uk")
            return 


    def check_valid_password(self,password):
        reject = []
        if len(password) < 8:

            reject.append("atleast 8 charactrs")
        lower =  any(c.islower() for c in password)
        upper = any(c.upper() for c in password)
        special = any(c in string.punctuation for c in password)
        digit = any(c.isdigit() for c in password)
        if not lower:

            reject.append("a lowercase letter")
        if not upper:

            reject.append("upper case letter")
        if not special:

            reject.append("special character")
        if not digit:

            reject.append("a digit")
        if reject:
            return "password needs:\n- "+"\n-".join(reject)
        return None
        


class LoginWindow(QWidget):
    def __init__(self, verify_login, on_register):
        super().__init__()

        self.resize(WIDTH, HEIGHT)

        self.switch_screen = switch_screen
        self.setWindowTitle("MAKE IT ALL")
        self.resize(WIDTH, HEIGHT)
        self.attempts = 0
        self.on_register = on_register

        self.username = QLineEdit(placeholderText="Username")
        self.password = QLineEdit(placeholderText="Password", echoMode=QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)

        self.register_button = QPushButton("Register")
        self.register_button.clicked.connect(self.register)

        title = QLabel("MAKE-IT-ALL")
        font = title.font()
        font.setBold(True)
        font.setPointSize(22)
        title.setFont(font)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        heading = QLabel("Login")
        heading_font = heading.font()
        heading_font.setBold(True)
        heading_font.setPointSize(16)
        heading.setFont(heading_font)
        heading.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.username.setMinimumHeight(40)
        self.password.setMinimumHeight(40)
        self.login_button.setMinimumHeight(40)
        self.register_button.setMinimumHeight(40)

        layout = QVBoxLayout(self)
        #layout.addWidget(QLabel("Login"))
        layout.addStretch()
        layout.addWidget(title)
        layout.addWidget(heading)
        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)


    def login(self):
        role = check_user(self.username.text(),self.password.text())
        if role == "team_leader":
            self.username.clear()
            self.password.clear()
            self.switch_screen(role, self.username.text())
        elif role == "team_member":
            self.username.clear()
            self.password.clear()
            self.switch_screen(role, self.username.text())
        else:
            QMessageBox.warning(self,"Login fail","Wrong username/password")
            self.password.clear()

    def register(self):
        #self.register = RegisterWindow()
        #self.register.show()
        self.on_register()
