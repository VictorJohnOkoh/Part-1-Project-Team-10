import sys
from PyQt6.QtWidgets import QApplication, QStackedWidget, QMainWindow
from .gui.login_gui import LoginWindow, RegisterWindow
from PyQt6.QtCore import QTimer
from productivity_app.gui.login_gui import LoginWindow
from productivity_app.gui.dashboard_gui import Dashboard
from productivity_app.gui.Post_gui import PostWindow
from productivity_app.users.Manager import Manager
from productivity_app.users.Employee import employees1, employees2
from productivity_app.users.TeamLead import Team_Leader
from productivity_app.users.Project import proj1, proj2
from productivity_app.users.Team import Team
from productivity_app.services.find_employeee import get_employee

WIDTH, HEIGHT = 300, 300
manager1 = Manager(4444, 'Anakin', 'Skywalker', 'anakin.skywalker@make-it-all.co.uk')
leader1 = Team_Leader(1111, 'John', 'Smith', 'john.smith@make-it-all.co.uk')
leader2 = Team_Leader(4444, 'Michael', 'Scott', 'michael.scott@make-it-all-co.uk')
team1 = Team(proj1, employees1, leader1)
team2 = Team(proj2, employees2, leader2)

employees = employees1 + employees2 + [manager1, leader1, leader2]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MAKE-IT-ALL")
        self.resize(WIDTH, HEIGHT)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.login_window = LoginWindow(self.switch_screen, self.switch_to_register)
        self.dashboard_window = None
        self.register_window = RegisterWindow(self.switch_to_login)

        self.stack.addWidget(self.login_window)
        self.stack.addWidget(self.register_window)
        self.stack.addWidget(self.register_window)
        self.stack.setCurrentWidget(self.login_window)

    def switch_screen(self, role: str, username: str):
        if self.dashboard_window is None and role == "team_leader":
            self.dashboard_window = Dashboard(leader1, self.logout)
            self.stack.addWidget(self.dashboard_window)
            self.stack.setCurrentWidget(self.dashboard_window)
        elif self.dashboard_window is None and role == "team_member":
            employee = get_employee(employees, username)
            self.dashboard_window = Dashboard(employee, self.logout)
            self.stack.addWidget(self.dashboard_window)
            self.stack.setCurrentWidget(self.dashboard_window)
        else:
            self.stack.setCurrentWidget(self.dashboard_window)


    def switch_to_register(self):
        self.stack.setCurrentWidget(self.register_window)
        
    def logout(self):
        self.stack.setCurrentWidget(self.login_window)
        self.stack.removeWidget(self.dashboard_window) 
        self.dashboard_window = None
        
        QTimer.singleShot(0, lambda: self.resize(WIDTH, HEIGHT))

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

