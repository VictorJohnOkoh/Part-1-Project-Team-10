from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton, QMessageBox,
)

from src.productivity_app.users import Task, Employee


class List(QWidget):
    def __init__(self, tasks: type[Task], employee: Employee):
        super().__init__()
        self.employee = employee
        self.tasks = self.employee.get_tasks()
        self.setWindowTitle(self.employee.get_full_name() + "'s dashboard")
    layout = QVBoxLayout()