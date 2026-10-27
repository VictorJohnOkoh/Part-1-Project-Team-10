from PyQt6 import QtWidgets
from PyQt6 import QtCore
from PyQt6 import QtGui
from productivity_app.users.Manager import Manager
from productivity_app.users.Employee import Employee

#(Are yet to be attached)
#from .gui.to_do_gui import to_do
#from .gui.post_gui import post
#from .gui.tasks_gui import tasks
#from .gui.training_gui import training
#from .gui.progress_gui import progress
#from .gui.assign_tasks_gui import assign_tasks
#from .gui.register_employee_gui import register_employee

# The actual dashboard window
class Dashboard(QtWidgets.QWidget):

# Runs automatically when someone writes Dashboard()
    def __init__(self, user, logout_service):
# Let QWidget do its own setup first, otherwise Qt breaks
        super().__init__()

        self.setWindowTitle("Dashboard")

        self.resize(800, 600)

        self.user = user
        self.logout = logout_service

# Build everything that goes inside the window
        self.build_ui()


# Keeps all the ui building in one place because AI said it was a good idea :)
    def build_ui(self):
        main_layout = QtWidgets.QVBoxLayout()

#title at the top of the screen that says "Welcome, 67 Sahurr"
        welcome_string = f"Welcome, {self.user.get_first_name()}" 
        title_label = QtWidgets.QLabel(welcome_string)
        title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        title_label.setFont(QtGui.QFont("Arial",22))


        task_box_1 = QtWidgets.QHBoxLayout()
        task_box_2 = QtWidgets.QHBoxLayout()
        task_box_3 = QtWidgets.QHBoxLayout()
#adding all the buttons 
        to_do_button = QtWidgets.QPushButton("To-do List")
        post_button = QtWidgets.QPushButton("View Post")
        tasks_button = QtWidgets.QPushButton("View Tasks")
        training_button = QtWidgets.QPushButton("Training")
        progress_button = QtWidgets.QPushButton("Project Progress")
        assign_tasks_button = QtWidgets.QPushButton("Assign Tasks")
        register_employee_button = QtWidgets.QPushButton("Register employee")
        logout_button = QtWidgets.QPushButton("Logout")

# connected the buttons to their functions (the functions that call their gui to pop up)
        to_do_button.clicked.connect(self.to_do_clicked)
        post_button.clicked.connect(self.post_clicked)
        tasks_button.clicked.connect(self.tasks_clicked)
        training_button.clicked.connect(self.training_clicked)
        progress_button.clicked.connect(self.progress_clicked)
        assign_tasks_button.clicked.connect(self.assign_tasks_clicked)
        register_employee_button.clicked.connect(self.register_employee_clicked)
        logout_button.clicked.connect(self.logout)


        all_buttons = [to_do_button, post_button, tasks_button, training_button, progress_button, assign_tasks_button, register_employee_button]
        for button in all_buttons:
            button.setSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                 QtWidgets.QSizePolicy.Policy.Expanding)
            button.setFont(QtGui.QFont("Arial",16))
            
        # Put the widgets into the layout, in order (top first)
        main_layout.addWidget(title_label,1)
        main_layout.addLayout(task_box_1,2)
        main_layout.addLayout(task_box_2,2)
        main_layout.addLayout(task_box_3,2)

        task_box_1.addWidget(to_do_button,1)
        task_box_1.addWidget(post_button, 1)
        task_box_1.addWidget(tasks_button, 1)


# only adding the register, project progress and assign task buttons if the user is of the manager class
        if isinstance(self.user, Manager):
            task_box_3.addWidget(register_employee_button, 1)
            task_box_2.addWidget(progress_button, 1)
            task_box_2.addWidget(assign_tasks_button, 1)
            task_box_2.addWidget(training_button, 1)
        #elif isinstance(self.user, Team_Leader): this is for if they are team leader but remains unimplemented
        #this is for basic team members
        else:
            pass

        task_box_3.addWidget(logout_button, 1)
        # Attach the layout to this window, so Qt actually displays it
        self.setLayout(main_layout)


    # The functions that run depending on which button is clicked
    #e.g. if to_do_button is clicked, 
    # its respective function is run so that the function may show the ui for the to-do functionality

    def to_do_clicked(self):
        print("todo clicked")

    def post_clicked(self):
        print("post clicked")

    def tasks_clicked(self):
        print("tasks clicked")

    def training_clicked(self):
        print("training clicked")

    def progress_clicked(self):
        print("progress clicked")

    def assign_tasks_clicked(self):
        print("assign tasks clicked")

    def register_employee_clicked(self):
        print("register employee clicked")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Dashboard(Manager(1234, 'John', 'Doe', 'john.doe@example.com'))
    window.show()
    sys.exit(app.exec())