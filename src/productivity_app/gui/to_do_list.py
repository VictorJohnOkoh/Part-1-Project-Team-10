import sys

from productivity_app.gui.dashboard_gui import Dashboard
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import(
    QButtonGroup,
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

STATUS = ["Not Started","In Progress","Finished"]
class TaskRow(QWidget):
    def __init__(self,text):
        super().__init__()

        #initialise new task status as not started
        self.status = STATUS[0]

        row = QHBoxLayout(self)
        self.label = QLabel(text)
        row.addWidget(self.label,stretch = 1)

        #creates the group used for each of the statuses as exclusive so only one can be  clicked at a time
        self.group = QButtonGroup(self)
        self.group.setExclusive(True)
        self.buttons = {}

        #loops over the exisiting statuses we have and creates a button for each of them
        #when one of the buttons are clicked the statuses are then changed
        for s in STATUS:
            b = QPushButton(s)
            b.setCheckable(True)
            b.setFixedSize(100,30)
            b.clicked.connect(lambda checked, s=s: self.set_status(s))
            self.group.addButton(b)
            row.addWidget(b)
            self.buttons[s] = b

        self.buttons[self.status].setChecked(True)

    """
    runs when a status button is clicked and updates the stored status
    the buttons are exclusive so when a new status is clicked it unchecks all of the other buttons
    """
    def set_status(self,status):
        self.status = status
        self.buttons[status].setChecked(True)

        #crosses out the tasks that are finished when the button is clicked

        font = self.label.font()
        font.setStrikeOut(status == "Finished")
        self.label.setFont(font)


class ToDoListWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(WIDTH,HEIGHT)
        self.setWindowTitle("To-Do List")
        self.new_task = QLineEdit(placeholderText = "New Task")
        self.new_task.move(300,350)

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