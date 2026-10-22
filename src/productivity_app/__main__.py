import sys
from PyQt6.QtWidgets import QApplication, QStackedWidget, QMainWindow
from .gui.login_gui import LoginWindow
from .gui.dashboard_gui import Dashboard
from .users.Manager import Manager
from .users.Employee import Employee

WIDTH, HEIGHT = 300, 300


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MAKE-IT-ALL")
        self.resize(WIDTH, HEIGHT)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.login_window = LoginWindow(self.switch_to_manager)
        self.dashboard_window = None

        self.stack.addWidget(self.login_window)
        self.stack.setCurrentWidget(self.login_window)

    def switch_to_manager(self):
        if self.dashboard_window is None:
            self.dashboard_window = Dashboard(Manager(1234, 'John', 'Doe', 'johndoe@make-it-all.co.uk'))
            self.stack.addWidget(self.dashboard_window)
            self.stack.setCurrentWidget(self.dashboard_window)
        else:
            self.stack.setCurrentWidget(self.dashboard_window)

    def switch_to_login(self):
        pass

    def switch_to_user(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

