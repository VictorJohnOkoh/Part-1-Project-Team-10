import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel,QPushButton,
    QLineEdit,QVBoxLayout,QGridLayout,
    QMessageBox
    
    )

#this class is for the window where the users can enter their login details to enter the system
class Window(QWidget):
    #this function is to initialise the window where the details are entered
    def __init__(self):
        super().__init__()
        self.resize(300,300)
        self.setWindowTitle("Make It All ")
        self.username = QLineEdit(placeholderText="Username")
        self.password = QLineEdit(placeholderText="Password")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        button = QPushButton("Login")
        button.clicked.connect(self.login)

        layout = QVBoxLayout(self)
        #layout.addWidget(title)
        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(button)

    #this function is where the checks are ran to make sure the user is authorised
    def login(self):
        if self.username.text() == "admin" and self.password.text() == "secret":
            print("S")
        else:
            QMessageBox.warning(self,"Login fail","Wrong username/password")
            self.password.clear()



app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec())