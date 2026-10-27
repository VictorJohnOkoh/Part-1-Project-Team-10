import sys
from PyQt6 import QtWidgets, QtCore, QtGui
from productivity_app.services.Project_Progress_Functions import Projects, Search_Project_Details

class ProgressWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MAKE IT ALL - Project Progress")
        self.resize(800, 600)
        self.User_Interface_Values()

    def User_Interface_Values(self):
        main_layout = QtWidgets.QVBoxLayout()
        for Single_Project in Projects:
            tasks = []
            project_name = Single_Project
            Details_Found = Projects[project_name]
            Team_Leader = Details_Found["teamLead"]
            Deadline = Details_Found["Deadline"]
            Estimated_hours = Details_Found["Estimated_hours"]
            tasks = Details_Found["tasks"]
            self.Build_UI(project_name, Team_Leader, Deadline, Estimated_hours, tasks, main_layout)
        self.setLayout(main_layout)

    def Build_UI(self, project_name, Team_Leader, Deadline, Estimated_hours, tasks, main_layout):
        Project_Name_label = QtWidgets.QLabel(project_name)
        Project_Name_label.setFont(QtGui.QFont("Arial", 20, QtGui.QFont.Weight.Bold))
        Project_Name_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(Project_Name_label)

        Project_Info_label = QtWidgets.QLabel(f"Team Leader Name: {Team_Leader} - Deadline: {Deadline} - Estimated Hours: {Estimated_hours}")
        Project_Info_label.setFont(QtGui.QFont("Arial", 12))
        Project_Info_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        main_layout.addWidget(Project_Info_label)

        table = QtWidgets.QTableWidget(len(tasks), 5)
        table.setHorizontalHeaderLabels(["Task Name", "Employee", "Deadline", "Estimated_hours", "Status"])
        table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

        count = 0
        for single_task in tasks:
            table.setItem(count, 0, QtWidgets.QTableWidgetItem(single_task["taskName"]))
            table.setItem(count, 1, QtWidgets.QTableWidgetItem(single_task["Employee"]))
            table.setItem(count, 2, QtWidgets.QTableWidgetItem(single_task["Deadline"]))
            table.setItem(count, 3, QtWidgets.QTableWidgetItem(str(single_task["Estimated_hours"])))
            table.setItem(count, 4, QtWidgets.QTableWidgetItem(single_task["Status"]))
            count += 1

        main_layout.addWidget(table)

# The execution guard so you can test it directly!
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ProgressWindow()
    window.show()
    sys.exit(app.exec())