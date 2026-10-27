import sys
from PyQt6.QtWidgets import QApplication, QStackedWidget, QMainWindow
from PyQt6.QtCore import QTimer
from productivity_app.gui.login_gui import LoginWindow
from productivity_app.gui.dashboard_gui import Dashboard
from productivity_app.users.Manager import Manager
from productivity_app.users.Employee import build_employee
from productivity_app.services.find_employeee import get_employee
from productivity_app.users.TeamLead import Team_Leader
from productivity_app.users.Project import proj1
from productivity_app.users.Team import Team

WIDTH, HEIGHT = 300, 300
employees = build_employee()
manager1 = Manager(4444, 'Anakin', 'Skywaler', 'anakin.skywalker@make-it-all.co.uk')
leader1 = Team_Leader(1111, 'John', 'Smith', 'john.smith@make-it-all.co.uk')
team1 = Team(proj1, employees, leader1)

for employee in employees:
    print(employee.__str__())

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MAKE-IT-ALL")
        self.resize(WIDTH, HEIGHT)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.login_window = LoginWindow(self.switch_screen)
        self.dashboard_window = None

        self.stack.addWidget(self.login_window)
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

    def logout(self):
        self.stack.setCurrentWidget(self.login_window)
        self.stack.removeWidget(self.dashboard_window) 
        self.dashboard_window = None
        
        QTimer.singleShot(0, lambda: self.resize(WIDTH, HEIGHT))

    def switch_to_login(self):
        pass

    def switch_to_user(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

