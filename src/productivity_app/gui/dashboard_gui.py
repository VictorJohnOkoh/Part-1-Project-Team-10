import sys
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QTableWidget,
)
from PyQt6.QtGui import QFont
from productivity_app.users import Manager

WIDTH, HEIGHT = 800, 600
font = QFont("Arial", 60)

class Dashboard(QWidget):
    def __init__(self, manager: type[Manager]):
        super().__init__()
        self.manager = manager
        self.setWindowTitle("MAKE-IT-ALL")
        self.resize(WIDTH, HEIGHT)

        layout = QVBoxLayout(self)

        # The table the dashboard is shown on
        table = QTableWidget()
        table.setRowCount(len(self.manager.get_tasks()))
        table.setColumnCount(1)
        table.setHorizontalHeaderLabels(["Project Name"])

        layout.addWidget(QLabel("Dashboard"))
        layout.addWidget(table)
