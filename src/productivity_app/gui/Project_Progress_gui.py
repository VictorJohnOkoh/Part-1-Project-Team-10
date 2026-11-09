from operator import index
import sys
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import (QApplication, QBoxLayout, QComboBox, QPushButton, QVBoxLayout, QWidget, 
                             QLabel, QScrollArea, QMainWindow, QSlider,
                             QLineEdit, QHBoxLayout, QGridLayout)
from productivity_app.services.Project_Progress_Functions import Projects, Search_Project_Details
from ..users.Manager import Manager

class ProgressWindow(QtWidgets.QWidget):
    def __init__(self, user, parent=None):
        super().__init__(parent)
        self.user = user
        self.setWindowTitle("MAKE IT ALL - Project Progress")
        self.resize(800, 600)
        self.User_Interface_Values()

    def User_Interface_Values(self):
        Scroll_Content = QWidget()
        main_layout = QVBoxLayout(self)
        Widget_Layout = QHBoxLayout()
        self.Content_Layout = QVBoxLayout(Scroll_Content)

        self.Topic_Input = QComboBox()
        self.Topic_Input.setEditable(True)
        self.Topic_Input.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
        Topic_Inputs = Projects.keys()
        self.Topic_Input.addItem("")
        for topic in Topic_Inputs:
            self.Topic_Input.addItem(topic)
        self.Topic_Input.completer().setCompletionMode(QtWidgets.QCompleter.CompletionMode.PopupCompletion)
        self.Topic_Input.completer().setFilterMode(Qt.MatchFlag.MatchContains)
        self.Topic_Input.lineEdit().setPlaceholderText("Search for a project...")
        self.Topic_Input.setCurrentIndex(-1)
        self.Topic_Input.currentIndexChanged.connect(
            lambda: self.Topic_Input.setCurrentIndex(-1) if self.Topic_Input.currentText() == "" else None
        )
        self.Topic_Input.setMaximumHeight(30)
        self.Topic_Input.setMaximumWidth(300)
        Widget_Layout.addWidget(self.Topic_Input)

        self.Employee_Input = QComboBox()
        self.Employee_Input.setEditable(True)
        self.Employee_Input.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
        self.Employee_Input.addItem("")
        for project in Projects.values():
            for task in project["tasks"]:
                employee_name = task["Employee"]
                if employee_name not in [self.Employee_Input.itemText(i) for i in range(self.Employee_Input.count())]:
                    self.Employee_Input.addItem(employee_name)
        self.Employee_Input.completer().setCompletionMode(QtWidgets.QCompleter.CompletionMode.PopupCompletion)
        self.Employee_Input.completer().setFilterMode(Qt.MatchFlag.MatchContains)
        self.Employee_Input.lineEdit().setPlaceholderText("Search for an Employee...")
        self.Employee_Input.setCurrentIndex(-1)
        self.Employee_Input.currentIndexChanged.connect(
            lambda: self.Employee_Input.setCurrentIndex(-1) if self.Employee_Input.currentText() == "" else None
        )
        self.Employee_Input.setMaximumHeight(30)
        self.Employee_Input.setMaximumWidth(300)
        Widget_Layout.addWidget(self.Employee_Input)

        Submit_Search_Button = QPushButton("Search")
        Submit_Search_Button.setMaximumHeight(30)
        Submit_Search_Button.setMaximumWidth(100)
        Submit_Search_Button.clicked.connect(lambda: self.Load_Projects(self.user, self.Topic_Input, self.Employee_Input, self.Content_Layout, issearch=True))
        Widget_Layout.addWidget(Submit_Search_Button)
        main_layout.addLayout(Widget_Layout)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)


        self.Load_Projects(self.user, self.Topic_Input, self.Employee_Input, self.Content_Layout)

        #self.Content_Layout.addStretch()
        #self.Content_Layout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        scroll.setWidget(Scroll_Content)
        main_layout.addWidget(scroll)

    def Load_Projects(self, user, Topic_Input, Employee_Input, Content_Layout, issearch=False):
        if not Topic_Input.currentText() and not Employee_Input.currentText():
            issearch = False

        while Content_Layout.count():
            item = Content_Layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        if issearch == False:
            if isinstance(self.user, (Manager)):
                for Single_Project in Projects:
                    tasks = []
                    project_name = Single_Project
                    Details_Found = Projects[project_name]
                    Team_LeaderName = Details_Found["teamLead"]
                    Deadline = Details_Found["Deadline"]
                    Estimated_hours = Details_Found["Estimated_hours"]
                    tasks = Details_Found["tasks"]
                    self.Build_UI(project_name, Team_LeaderName, Deadline, Estimated_hours, tasks, Content_Layout)

            else:
                for Single_Project in Projects:
                    if self.user.get_full_name() in Projects[Single_Project]["teamLead"]:
                        tasks = []
                        project_name = Single_Project
                        Details_Found = Projects[project_name]
                        Team_LeaderName = Details_Found["teamLead"]
                        Deadline = Details_Found["Deadline"]
                        Estimated_hours = Details_Found["Estimated_hours"]
                        tasks = Details_Found["tasks"]
                        if Team_LeaderName == self.user.get_full_name():
                            self.Build_UI(project_name, Team_LeaderName, Deadline, Estimated_hours, tasks, Content_Layout)

        else:
            search_topic = Topic_Input.currentText().strip()
            search_employee = Employee_Input.currentText().strip()

            if isinstance(self.user, (Manager)):
                for Single_Project in Projects:
                    tasks = []
                    project_name = Single_Project
                    Details_Found = Projects[project_name]
                    Team_LeaderName = Details_Found["teamLead"]
                    Deadline = Details_Found["Deadline"]
                    Estimated_hours = Details_Found["Estimated_hours"]
                    tasks = Details_Found["tasks"]

                    if search_topic and search_employee:
                        if (search_topic.lower() in project_name.lower()) and any(search_employee.lower() in task["Employee"].lower() for task in tasks):
                            self.Build_UI(project_name, Team_LeaderName, Deadline, Estimated_hours, tasks, Content_Layout)
                    elif search_topic:
                        if search_topic.lower() in project_name.lower():
                            self.Build_UI(project_name, Team_LeaderName, Deadline, Estimated_hours, tasks, Content_Layout)
                    elif search_employee:
                        if any(search_employee.lower() in task["Employee"].lower() for task in tasks):
                            self.Build_UI(project_name, Team_LeaderName, Deadline, Estimated_hours, tasks, Content_Layout)

            else:
                for Single_Project in Projects:
                    if self.user.get_full_name() in Projects[Single_Project]["teamLead"]:
                        tasks = []
                        project_name = Single_Project
                        Details_Found = Projects[project_name]
                        Team_LeaderName = Details_Found["teamLead"]
                        Deadline = Details_Found["Deadline"]
                        Estimated_hours = Details_Found["Estimated_hours"]
                        tasks = Details_Found["tasks"]

                        if Team_LeaderName == self.user.get_full_name():
                            if search_topic and search_employee:
                                if (search_topic.lower() in project_name.lower()) and any(search_employee.lower() in task["Employee"].lower() for task in tasks):
                                    self.Build_UI(project_name, Team_LeaderName, Deadline, Estimated_hours, tasks, Content_Layout)
                            elif search_topic:
                                if search_topic.lower() in project_name.lower():
                                    self.Build_UI(project_name, Team_LeaderName, Deadline, Estimated_hours, tasks, Content_Layout)
                            elif search_employee:
                                if any(search_employee.lower() in task["Employee"].lower() for task in tasks):
                                    self.Build_UI(project_name, Team_LeaderName, Deadline, Estimated_hours, tasks, Content_Layout)
        Content_Layout.addStretch()

    def Build_UI(self, project_name, Team_Leader, Deadline, Estimated_hours, tasks, Content_layout):

        Project_Name_label = QtWidgets.QLabel(project_name)
        Project_Name_label.setFont(QtGui.QFont("Arial", 20, QtGui.QFont.Weight.Bold))
        Project_Name_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        Content_layout.addWidget(Project_Name_label)

        Project_Info_label = QtWidgets.QLabel(f"Team Leader Name: {Team_Leader} - Deadline: {Deadline} - Total Estimated Hours: {Estimated_hours}")
        Project_Info_label.setFont(QtGui.QFont("Arial", 12))
        Project_Info_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        Content_layout.addWidget(Project_Info_label)

        Progress_Bar = QtWidgets.QProgressBar()
        completed_hours = 0
        for single_task in tasks:
            if single_task["Status"].strip() == "Complete":
                completed_hours += single_task["Estimated_hours"]
        
        percent_complete = (completed_hours/Estimated_hours) * 100
        Progress_Bar.setValue(int(percent_complete))
        Progress_Bar.setFixedHeight(25)
        Content_layout.addWidget(Progress_Bar)

        table = QtWidgets.QTableWidget(len(tasks), 5)
        table.setHorizontalHeaderLabels(["Task Name", "Employee", "Deadline", "Estimated_hours", "Status"])
        table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        count = 0
        for single_task in tasks:
            table.setItem(count, 0, QtWidgets.QTableWidgetItem(single_task["taskName"]))
            table.setItem(count, 1, QtWidgets.QTableWidgetItem(single_task["Employee"]))
            table.setItem(count, 2, QtWidgets.QTableWidgetItem(single_task["Deadline"]))
            table.setItem(count, 3, QtWidgets.QTableWidgetItem(str(single_task["Estimated_hours"])))
            table.setItem(count, 4, QtWidgets.QTableWidgetItem(single_task["Status"]))
            count += 1

        total_height = table.horizontalHeader().height() + 2

        for i in range(table.rowCount()):
            total_height += table.rowHeight(i)
        
        table.setFixedHeight(total_height)
        table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        Content_layout.addWidget(table)

# The execution guard so you can test it directly!
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ProgressWindow()
    window.show()
    sys.exit(app.exec())