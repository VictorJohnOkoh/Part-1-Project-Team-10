from PyQt6 import QtWidgets
from PyQt6 import QtCore
from PyQt6 import QtGui



#today, i will add scrolling
# add helper method to add fillers for other entries
#make it look slightly nicer
#add a placeholder dict for all the attributes i will display for training.
# i think this will take 2-3hrs



class ViewInfo(QtWidgets.QWidget):
    # Runs automatically when someone writes Dashboard()
    def __init__(self,user):
# Let QWidget do its own setup first, otherwise Qt breaks
        super().__init__()

        self.setWindowTitle("Info Board")

        self.resize(800, 600)

        self.user = user

        self.build_ui()

    def build_ui(self):
        main_layout = QtWidgets.QVBoxLayout()

        welcome_string = f"Viewing: Billy Rossa" 
        title_label = QtWidgets.QLabel(welcome_string)
        title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        title_label.setFont(QtGui.QFont("Arial",25))
        title_label.setFrameShape(QtWidgets.QFrame.Shape.Box)
        title_label.setLineWidth(1)
        title_label.setAutoFillBackground(True)

        
        palette_title = title_label.palette()
        palette_title.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor("#3a3a3a")) 
        palette_title.setColor(QtGui.QPalette.ColorRole.WindowText, QtGui.QColor("#e0e0e0")) 

        title_label.setPalette(palette_title)


        go_back_button = QtWidgets.QPushButton("Go Back")
        palette_go_back = go_back_button.palette()
        palette_go_back.setColor(QtGui.QPalette.ColorRole.Button, QtGui.QColor("#5D3434"))  
        palette_go_back.setColor(QtGui.QPalette.ColorRole.ButtonText, QtGui.QColor("#e0e0e0"))
        go_back_button.setPalette(palette_go_back)
        go_back_button.setSizePolicy(
                    QtWidgets.QSizePolicy.Policy.Fixed,
                    QtWidgets.QSizePolicy.Policy.Expanding)

        go_back_button.clicked.connect(self.close)

        data_entry_1 = QtWidgets.QLabel("Name: Billy Rossa")
        data_entry_2 = QtWidgets.QLabel("Position: Team Leader")
        data_entry_3 = QtWidgets.QLabel("Average Task per Week: 7")
        data_entry_4 = QtWidgets.QLabel("Current Task Amount: 4")
        data_entry_5 = QtWidgets.QLabel("Hours per week: 102hr")

        data_entries = [data_entry_1, data_entry_2, data_entry_3, data_entry_4, data_entry_5]

        layout_1 = QtWidgets.QHBoxLayout()
        layout_2 = QtWidgets.QVBoxLayout()

        layout_1.addWidget(title_label)
        layout_1.addWidget(go_back_button)

        main_layout.addLayout(layout_1,1)
        main_layout.addLayout(layout_2,5)

        for entry in data_entries:
            entry.setFrameShape(QtWidgets.QFrame.Shape.Box)
            entry.setLineWidth(1)
            layout_2.addWidget(entry)
        
        
        self.setLayout(main_layout)

class TrainingQuestion(QtWidgets.QWidget):
    # Runs automatically when someone writes Dashboard()
    def __init__(self,user):
# Let QWidget do its own setup first, otherwise Qt breaks
        super().__init__()

        self.setWindowTitle("Training topic")

        self.resize(170, 120)

        self.user = user

        self.build_ui()

    def build_ui(self):
        main_layout = QtWidgets.QVBoxLayout()

        question_label = QtWidgets.QLabel("What Topic does this person need training on?")
        name_input = QtWidgets.QLineEdit()
        name_input.setPlaceholderText("Enter Topic")
        text = name_input.text()
        
        main_layout.addWidget(question_label,1)
        main_layout.addWidget(name_input,1)

        self.setLayout(main_layout)
        



class Training(QtWidgets.QWidget):

# Runs automatically when someone writes Dashboard()
    def __init__(self,user):
# Let QWidget do its own setup first, otherwise Qt breaks
        super().__init__()

        self.setWindowTitle("Training Board")

        self.resize(800, 600)

        self.user = user

        self.build_ui()

    def build_ui(self):
        main_layout = QtWidgets.QVBoxLayout()


        welcome_string = f"{self.user.get_first_name()}" 
        title_label = QtWidgets.QLabel(welcome_string)
        title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        title_label.setFont(QtGui.QFont("Arial Black",30))
        title_label.setFrameShape(QtWidgets.QFrame.Shape.Box)
        title_label.setLineWidth(1)
        title_label.setAutoFillBackground(True)
        palette = title_label.palette()
        palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor("#3a3a3a"))      # background
        palette.setColor(QtGui.QPalette.ColorRole.WindowText, QtGui.QColor("#e0e0e0"))  # text
        title_label.setPalette(palette)

        task_box_1 = QtWidgets.QHBoxLayout()
        task_box_2 = QtWidgets.QVBoxLayout()


        #placeholder_name = QtWidgets.QLabel("name")
        #team_name = QtWidgets.QLabel("team")


        view_info_button_1 = QtWidgets.QPushButton("View Info")
        view_info_button_2 = QtWidgets.QPushButton("View Info")
        view_info_button_3 = QtWidgets.QPushButton("View Info")
        view_info_button_4 = QtWidgets.QPushButton("View Info")
        view_info_buttons = [view_info_button_1, view_info_button_2, view_info_button_3, view_info_button_4]

        training_button_1 = QtWidgets.QPushButton("Training")
        training_button_2 = QtWidgets.QPushButton("Training")
        training_button_3 = QtWidgets.QPushButton("Training")
        training_button_4 = QtWidgets.QPushButton("Training")
        training_buttons = [training_button_1, training_button_2, training_button_3, training_button_4]

        for button in training_buttons:
                    button.clicked.connect(self.training_clicked)
                    button.setSizePolicy(
                    QtWidgets.QSizePolicy.Policy.Expanding,
                    QtWidgets.QSizePolicy.Policy.Expanding)

        for button in view_info_buttons:
            button.clicked.connect(self.view_info_clicked)
            button.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Expanding)

        #entry_chunk_list = [placeholder_name, team_name, role_name, view_info_button]

        entry_1_layout = QtWidgets.QHBoxLayout()
        entry_2_layout = QtWidgets.QHBoxLayout()
        entry_3_layout = QtWidgets.QHBoxLayout()
        entry_4_layout = QtWidgets.QHBoxLayout()
        entry_layout_list = [entry_1_layout, entry_2_layout, entry_3_layout, entry_4_layout]

        entry_1 = QtWidgets.QFrame()
        entry_1.setLayout(entry_1_layout)
        entry_2 = QtWidgets.QFrame()
        entry_2.setLayout(entry_2_layout)
        entry_3 = QtWidgets.QFrame()
        entry_3.setLayout(entry_3_layout)
        entry_4 = QtWidgets.QFrame()
        entry_4.setLayout(entry_4_layout)
        entry_frame_list = [entry_1, entry_2, entry_3, entry_4]

        demo_entries = [
        ("Alice Smith", "Team A", "Yes"),
        ("Ben Jones", "Team B", "No"),
        ("Chloe Brown", "Team A", "Yes"),
        ("Dan Patel", "Team C", "No"),
        ]


        task_box_1.addWidget(title_label,1)

        main_layout.addLayout(task_box_1,1)
        main_layout.addLayout(task_box_2,5)
        

        for entry_layout_index in range(len(entry_layout_list)):
            entry_layout_list[entry_layout_index].addWidget(QtWidgets.QLabel(demo_entries[entry_layout_index][0]), 1)
            entry_layout_list[entry_layout_index].addWidget(QtWidgets.QLabel(demo_entries[entry_layout_index][1]), 1)
            entry_layout_list[entry_layout_index].addWidget(training_buttons[entry_layout_index], 1)
            entry_layout_list[entry_layout_index].addWidget(view_info_buttons[entry_layout_index], 1)
        
        
        for entry_frame in entry_frame_list:
            entry_frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
            entry_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
            entry_frame.setLineWidth(1)
            task_box_2.addWidget(entry_frame,1)


        self.setLayout(main_layout)


    def view_info_clicked(self):
        self.view_info = ViewInfo(self.user)
        self.view_info.show()
        print("training clicked")

    def training_clicked(self):
        self.training_question = TrainingQuestion(self.user)
        self.training_question.show()
        print("Training has been clicked")
        



