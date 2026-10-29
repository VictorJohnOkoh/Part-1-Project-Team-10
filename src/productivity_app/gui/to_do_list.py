import sys

from productivity_app.gui.dashboard_gui import Dashboard
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import(
    QHBoxLayout,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QApplication
)

WIDTH, HEIGHT = 500,350

class ToDoListWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(WIDTH,HEIGHT)
        self.setWindowTitle("To-Do List")
        self.new_task = QLineEdit(placeholderText = "New Task")

        #button to add new tasks
        button = QPushButton("Add new task")
        button.setFixedSize(100,30)
        button.move(250,300)
        #button.raise_()
        #go to function to add new task
        button.clicked.connect(self.add_task)
        
        #button to back to the users' dashboard
        back_button = QPushButton("Go back")
        back_button.setFixedSize(100,30)
        back_button.clicked.connect(self.go_back)

        input_row = QHBoxLayout()
        input_row.addWidget(self.new_task)
        input_row.addWidget(button)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("TO-DO LIST"),alignment= Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.new_task)
        layout.addWidget(button)
        layout.addWidget(back_button)
        layout.addLayout(input_row)

        self.tasks_layout = QVBoxLayout()
        layout.addLayout(self.tasks_layout)
        #layout.addStretch()

    def add_task(self):
        text = self.new_task.text().strip()
        if not text:
            return
        self.tasks_layout.addWidget(TaskRow(text))
        self.new_task.clear()


    #function to take the user to their dashboard
    def go_back(self):
        print("Back button clicked")


app = QApplication(sys.argv)
window = ToDoListWindow()
window.show()
sys.exit(app.exec())