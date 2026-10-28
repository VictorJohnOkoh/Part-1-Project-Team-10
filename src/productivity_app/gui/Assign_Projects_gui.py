#Assign Tasks
import random
import sys
from PyQt6.QtCore import QSize, Qt, QDateTime
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (QApplication, QPushButton, QVBoxLayout, QWidget, 
                             QLabel, QScrollArea, QMainWindow, QSlider,
                             QHBoxLayout, QLineEdit,QDateTimeEdit, QTextEdit, QMessageBox, QComboBox, QDialog)
import os
# Directory = os.productivity_app.gui('Assign_Tasks_gui.py')
# FilePath = os.productivity_app.users('test_users.txt')

Directory = os.path.dirname(os.path.abspath(__file__))

FilePath = os.path.join(Directory, "..", "users", "test_users.txt")

class AssignProjectsWindow(QWidget):

    Projects = []

    def GiveProjects(self):
        return self.Projects


    Is_Format_Correct = False
    def Is_Format_Correct_Message(self):
        Message = QMessageBox()
        Message.setWindowTitle('Project Assignment')

        if self.Is_Format_Correct == True:
            Message.setText('Project successfully Assigned!')
            Message.setIcon(QMessageBox.Icon.Information)
            print(self.Projects)
        else:
             Message.setText('Insufficient Data provided!')
             Message.setInformativeText('Please try again.')
             Message.setIcon(QMessageBox.Icon.Critical)
        Message.exec()


    def ProjectAssignerSubmitButton_clicked(self):
                self.Is_Format_Correct = False
                ProjectName = self.ProjectNameInput.text()
                EmpName = self.EmployeeNameInput.currentText()

                self.ProjectNameInput.clear()

                if len(ProjectName) != 0:
                    print('message assigned!')
                    self.Projects.append([ProjectName,EmpName])
                    self.Is_Format_Correct = True
                else:
                    print('Incorrect, try again!')
                self.Is_Format_Correct_Message()
                
    def __init__(self, parent=None):
        super().__init__(parent)


        self.AssignWidget = QWidget()
        self.AssignVbox = QVBoxLayout(self.AssignWidget)

        #Assign Button with Textboxes
        self.ProjectNameInput = QLineEdit()
        self.ProjectNameInput.setPlaceholderText('Project Name')
        self.ProjectNameInput.setFixedWidth(400)

        self.EmployeeNameInput = QComboBox()
        with open(FilePath,'r') as Users:
            for UserLine in Users:
                User = UserLine.split(':')
                if User[2] == 'team_leader\n':
                     self.EmployeeNameInput.addItem(User[0])
        self.EmployeeNameInput.setFixedWidth(400)



        # setting up the deadline chooser for the managers/ team leaders

        ProjectAssignerSubmitButton = QPushButton(text='Assign Project')
        ProjectAssignerSubmitButton.setFixedSize(400,60)
        ProjectAssignerSubmitButton.clicked.connect(self.ProjectAssignerSubmitButton_clicked)


        self.AssignVbox.addWidget(self.ProjectNameInput)
        self.AssignVbox.addWidget(self.EmployeeNameInput)
        self.AssignVbox.addWidget(self.ProjectNameInput)
        self.AssignVbox.addWidget(ProjectAssignerSubmitButton)

        self.setLayout(self.AssignVbox)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AssignProjectsWindow()
    window.show()
    sys.exit(app.exec())