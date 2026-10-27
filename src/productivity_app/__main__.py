import sys
from PyQt6.QtWidgets import QApplication, QStackedWidget, QMainWindow
from .gui.login_gui import LoginWindow, RegisterWindow
from .gui.login_gui import LoginWindow, RegisterWindow
from .gui.dashboard_gui import Dashboard
from .gui.Post_gui import PostWindow
from .users.Manager import Manager
from .users.Employee import Employee

WIDTH, HEIGHT = 300, 300
WIDTH, HEIGHT = 300, 300


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MAKE-IT-ALL")
        self.resize(WIDTH, HEIGHT)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.login_window = LoginWindow(self.switch_to_manager, self.switch_to_register)
        self.login_window = LoginWindow(self.switch_to_manager, self.switch_to_register)
        self.dashboard_window = None
        self.register_window = RegisterWindow(self.switch_to_login)
        self.register_window = RegisterWindow(self.switch_to_login)

        self.stack.addWidget(self.login_window)
        self.stack.addWidget(self.register_window)
        self.stack.addWidget(self.register_window)
        self.stack.setCurrentWidget(self.login_window)

    def switch_screen(self, role: str, username: str):
        if self.dashboard_window is None and role == "team_leader":
            self.dashboard_window = Dashboard(Manager(1234, 'John', 'Doe', 'johndoe@make-it-all.co.uk'))
            self.stack.addWidget(self.dashboard_window)
            self.stack.setCurrentWidget(self.dashboard_window)
        elif self.dashboard_window is None and role == "team_member":
            self.dashboard_window = Dashboard(Employee(5678, 'Jane', 'Smith', 'janesmith@make-it-all.co.uk'))
            self.stack.addWidget(self.dashboard_window)
            self.stack.setCurrentWidget(self.dashboard_window)
        else:
            self.stack.setCurrentWidget(self.dashboard_window)

    def switch_to_register(self):
        self.stack.setCurrentWidget(self.register_window)

    def switch_to_register(self):
        self.stack.setCurrentWidget(self.register_window)

    def switch_to_login(self):
        self.stack.setCurrentWidget(self.login_window)
        #pass
        self.stack.setCurrentWidget(self.login_window)
        #pass

    def switch_to_user(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

