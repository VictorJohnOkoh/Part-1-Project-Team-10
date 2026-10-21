from PyQt6 import QtWidgets
from PyQt6 import QtCore
from PyQt6 import QtGui


# Our dashboard window. It "is a" QWidget, so it gets all of QWidget's abilities
class Dashboard(QtWidgets.QWidget):

    # Runs automatically when someone writes Dashboard()
    def __init__(self,user):
        # Let QWidget do its own setup first, otherwise Qt breaks
        super().__init__()

        # Text shown in the window's title bar
        self.setWindowTitle("Dashboard")

        # Starting width and height in pixels (the user can still resize it)
        self.resize(800, 600)


        self.user = user

        # Build everything that goes inside the window
        self.build_ui()


    # Keeps all the widget/layout code in one place, separate from setup
    def build_ui(self):
        # Top-level layout: stacks things vertically, top to bottom
        main_layout = QtWidgets.QVBoxLayout()

        # A simple text widget, just to prove the window works
        welcome_string = f"Welcome, {self.user.first_name}" 
        title_label = QtWidgets.QLabel(welcome_string)
        title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        title_label.setFont(QtGui.QFont("Arial",22))

        # A button, also a placeholder for now
        refresh_button = QtWidgets.QPushButton("Refresh")

        # When the button is clicked, run our on_refresh method
        refresh_button.clicked.connect(self.on_refresh)

        task_box_1 = QtWidgets.QHBoxLayout()
        task_box_2 = QtWidgets.QHBoxLayout()
        task_box_3 = QtWidgets.QHBoxLayout()

        to_do_button = QtWidgets.QPushButton("To-do List")
        post_button = QtWidgets.QPushButton("View Post")
        tasks_button = QtWidgets.QPushButton("View Tasks")
        training_button = QtWidgets.QPushButton("Training")
        progress_button = QtWidgets.QPushButton("Project Progress")
        assign_tasks_button = QtWidgets.QPushButton("Assign Tasks")
        register_employee_button = QtWidgets.QPushButton("Register employee")


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

        task_box_2.addWidget(training_button, 1)
        task_box_2.addWidget(progress_button, 1)
        task_box_2.addWidget(assign_tasks_button, 1)

        task_box_3.addWidget(register_employee_button, 1)

        # Attach the layout to this window, so Qt actually displays it
        self.setLayout(main_layout)

    # A "slot": the code that runs when the button is clicked
    def on_refresh(self):
        print("Refresh clicked")


# Only runs if you run THIS file directly (handy for testing on its own).
# It's ignored when another file imports Dashboard.
if __name__ == "__main__":
    # Every Qt program needs exactly one QApplication, created before any widgets
    app = QtWidgets.QApplication([])

    # Create the dashboard and make it visible
    window = Dashboard()
    window.show()

    # Start Qt's event loop: waits for clicks/keys until the window closes
    app.exec()