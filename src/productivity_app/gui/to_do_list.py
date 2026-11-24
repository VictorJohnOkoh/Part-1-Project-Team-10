import sys
#import may have to get removed because it creates a circular import 
#because dashboard gui imports this file

#from productivity_app.gui.dashboard_gui import Dashboard
from PyQt6.QtCore import Qt,QDateTime,QDate
from PyQt6.QtWidgets import(
    QButtonGroup,
    QHBoxLayout,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QApplication,
    QTextEdit,
    QDateTimeEdit,
    QComboBox

)

WIDTH, HEIGHT = 800,450

hardcoded_tasks = [("attend meeting","In Progress"),
                   ("complete research","Not Started"),
                   ("ask customer for clarification","Finished")]

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


class addNewTaskWindow(QWidget):
    def __init__(self):
        super().__init__()
        #self.on_back = on_back

        self.AddNewTask = QWidget()
        self.add_new_task_vbox = QVBoxLayout(self.AddNewTask)

        self.resize(WIDTH,HEIGHT)

        #text box for task name
        self.enter_task_name = QLabel(text = "Enter the task name")
        self.new_task = QLineEdit(placeholderText = "New Task")
        self.new_task.setFixedWidth(750)

        #text box for task description
        self.enter_task_description = QLabel(text = "Enter the task description")
        self.add_description = QTextEdit(placeholderText = "Enter the description of the task")
        self.add_description.setFixedSize(750,150)

        #text box for estimated hours
        self.enter_estimated_hours = QLabel(text = "Enter the estimate time")
        self.estimated_time = QLineEdit(placeholderText = "Enter the estimated time in hours")
        self.estimated_time.setFixedWidth(750)

        #calendar to set deadline
        self.enter_deadline = QLabel(text = "Enter the deadline of this task")
        self.deadline_date_time = QDateTimeEdit()
        self.deadline_date_time.setCalendarPopup(True)
        self.deadline_date_time.setDateTime(QDateTime.currentDateTime())

        #dropdown menu to enter priority
        self.enter_priority = QLabel(text = "Enter the task priority")
        self.task_priority = QComboBox()
        self.task_priority.addItems(["Low","Medium","High"])
        # self.task_priority.currentIndexChanged.connect(self.index_changed)

        #button to add new task
        new_task_button = QPushButton("Add task")
        new_task_button.setFixedSize(100,30)
        #new_task_button.move(400,300)
        new_task_button.clicked.connect(self.add_new_task)
        #move button to the bottom of the screen
        #call function to take user back to to-do list with new task added

        #button to go back without adding new task
        cancel_button = QPushButton("Cancel")
        cancel_button.setFixedSize(100,30)
        cancel_button.move(400,300)
        cancel_button.clicked.connect(self.back_button)
        #call function to take user back to to-do list without adding the new task

        self.add_new_task_vbox.addWidget(self.enter_task_name)
        self.add_new_task_vbox.addWidget(self.new_task)
        self.add_new_task_vbox.addWidget(self.enter_task_description)
        self.add_new_task_vbox.addWidget(self.add_description)
        self.add_new_task_vbox.addWidget(self.enter_estimated_hours)
        self.add_new_task_vbox.addWidget(self.estimated_time)
        self.add_new_task_vbox.addWidget(self.enter_deadline)
        self.add_new_task_vbox.addWidget(self.deadline_date_time)
        self.add_new_task_vbox.addWidget(self.enter_priority)
        self.add_new_task_vbox.addWidget(self.task_priority)
        self.add_new_task_vbox.addWidget(new_task_button)
        self.add_new_task_vbox.addWidget(cancel_button)

        self.setWindowTitle("Add new task")
        self.setLayout(self.add_new_task_vbox)

    def back_button(self):
        #self.on_back()
        pass
    
    is_format_correct = False

    #function to output if any of the formats of the data entered is incorrect
    def is_format_correct_message(self):
        message = QMessageBox()
        message.setWindowTitle("Add new task")
        if self.is_format_correct == True:
            print("call function to go create new task row of the new task")
            #call function to back to task row class
        else:
            message.setText("Insufficient data provided")
            message.setInformativeText("Please try again")
            message.setIcon(QMessageBox.Icon.Critical)
            message.exec()

    #function to check if the estimated time entered is a valid integer or float value and not a string
    def check_estimated_time(self,estimated_time):
        return isinstance(estimated_time, (int, float))

    #function to check if the deadline is in the future when a new task is being created and not in the past
    def check_deadline_valid(self,chosen_deadline):
        now = QDate.currentDate()
        deadline = chosen_deadline.toString(Qt.DateFormat.ISODate)
        if deadline>=now:
            return True
        else:
            return False

    #function to check if all of the data fields are valid and relevant actions are then taken
    def add_new_task(self):
        self.is_format_correct = False
        task_name = self.enter_task_name.text()
        task_desc = self.add_description.toPlainText()
        estim_time = self.estimated_time.text()
        chosen_deadline = self.deadline_date_time.dateTime()
        priority = self.task_priority.currentText()

        if len(task_name)!=0 and len(task_desc)!=0 and self.check_estimated_time(estim_time) and self.check_deadline_valid(chosen_deadline):
            self.is_format_correct = True
        self.is_format_correct_message()

class ToDoListWindow(QWidget):
    def __init__(self):#removed ",add_task"
        super().__init__()
        # self.add_task = add_task

        self.ToDoList = QWidget()
        self.to_do_list_vbox = QVBoxLayout(self.ToDoList)

        self.resize(WIDTH,HEIGHT)

        #button to take the user to add new task screen when clicked
        add_new_task_button = QPushButton("Add task")
        add_new_task_button.setFixedSize(100,30)
        add_new_task_button.clicked.connect(self.add_task)
        
        self.to_do_list_vbox.addWidget(add_new_task_button)

        self.setWindowTitle("To-do List")
        self.setLayout(self.to_do_list_vbox)

    def add_task(self):
        #call function to add new task screen
        # self.add_task()
        print("function to add task window")

    #function to take the user to their dashboard
    def go_back(self):
        print("Back button clicked")

app = QApplication(sys.argv)
window = addNewTaskWindow()
window.show()
sys.exit(app.exec())