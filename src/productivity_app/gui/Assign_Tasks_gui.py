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

FilePath = os.path.join(Directory, "..", "users", "valid_users.txt")

class AssignTasksWindow(QWidget):

    Assignments = []

    ProjectNames = ['Team 1', 'Team 2', 'Team 3', 'Team 4', 'Team 5', 'Team 6',
 'Team 7', 'Team 8', 'Team 9', 'Team 10', 'Team 11', 'Team 12',
 'Team 13', 'Team 14', 'Team 15', 'Team 16', 'Team 17', 'Team 18',
 'Team 19', 'Team 20', 'Team 21', 'Team 22']

    @staticmethod
    def GiveAssignments():
        return AssignTasksWindow.Assignments


    Is_Format_Correct = False
    def Is_Format_Correct_Message(self):
        Message = QMessageBox()
        Message.setWindowTitle('Task Assignment')
        # OK_Button = Message.addButton('Ok',QMessageBox.ButtonRole.AcceptRole)
        # if Message.clickedButton() == OK_Button:
        #     print('hehe')

        if self.Is_Format_Correct == True:
            Message.setText('Task successfully Assigned!')
            Message.setIcon(QMessageBox.Icon.Information)
            print(self.Assignments)
        else:
             Message.setText('Insufficient Data provided!')
             Message.setInformativeText('Please try again.')
             Message.setIcon(QMessageBox.Icon.Critical)


    def TaskAssignerSubmitButton_clicked(self):
                self.Is_Format_Correct = False
                TaskName = self.TaskNameInput.text()
                TaskDesc = self.TaskDescriptionInput.toPlainText()
                EmpName = self.EmployeeNameInput.currentText()
                Team = self.ProjectNameInput.currentText()
                EstimatedTime = self.TaskEstimatedTimeInput.text()
                ChosenDeadline = self.ChosenDateAndTime.dateTime()

                self.TaskNameInput.clear()
                self.TaskDescriptionInput.clear()
                self.EmployeeNameInput.clear()
                self.ChosenDateAndTime.setDateTime(QDateTime.currentDateTime())

                if len(TaskName) != 0 and len(TaskDesc) != 0 and len(EstimatedTime) != 0:
                    print('message assigned!')
                    self.Assignments.append([TaskName,TaskDesc,EmpName,Team,ChosenDeadline.toString('dd-MM-yyyy HH:mm'),EstimatedTime,'Incomplete'])
                    self.Is_Format_Correct = True
                else:
                    print('Incorrect, try again!')
                self.Is_Format_Correct_Message()
                
    def __init__(self, parent=None):
        super().__init__(parent)


        self.AssignWidget = QWidget()
        self.AssignVbox = QVBoxLayout(self.AssignWidget)

        #Assign Button with Textboxes
        self.TaskNameInput = QLineEdit()
        self.TaskNameInput.setPlaceholderText('Name of task')
        self.TaskNameInput.setFixedWidth(400)

        self.TaskDescriptionInput = QTextEdit()
        self.TaskDescriptionInput.setPlaceholderText('Describe what needs to be done to finish the task')
        self.TaskDescriptionInput.setFixedWidth(400)
        self.TaskDescriptionInput.setFixedHeight(200)

        self.TaskEstimatedTimeInput = QLineEdit()
        self.TaskEstimatedTimeInput.setPlaceholderText('Enter the estimated time required for this task. (in hours)')
        self.TaskEstimatedTimeInput.setFixedWidth(400)

        self.EmployeeNameInput = QComboBox()
        with open(FilePath,'r') as Users:
            for UserLine in Users:
                User = UserLine.split(':')
                if User[2] == 'team_member\n':
                     self.EmployeeNameInput.addItem(User[0])
        self.EmployeeNameInput.setFixedWidth(400)


        self.ProjectNameInput = QComboBox()
        for project in self.ProjectNames:
            self.ProjectNameInput.addItem(project)
        self.ProjectNameInput.setFixedWidth(400)
        # setting up the deadline chooser for the managers/ team leaders


        self.GuideToDeadLineSelection = QLabel(text='Use the down arrow below to select a deadline from the calendar.')
        self.SecondGuideToDeadlineSelection = QLabel(text='Once chosen, use the arrows to make any necessary final adjustments.')
            
        self.ChosenDateAndTime = QDateTimeEdit()
        self.ChosenDateAndTime.setCalendarPopup(True)
        self.ChosenDateAndTime.setDateTime(QDateTime.currentDateTime())

        TaskAssignerSubmitButton = QPushButton(text='Assign Task')
        TaskAssignerSubmitButton.setFixedSize(400,60)
        TaskAssignerSubmitButton.clicked.connect(self.TaskAssignerSubmitButton_clicked)


        self.AssignVbox.addWidget(self.TaskNameInput)
        self.AssignVbox.addWidget(self.TaskDescriptionInput)
        self.AssignVbox.addWidget(self.TaskEstimatedTimeInput)
        self.AssignVbox.addWidget(self.EmployeeNameInput)
        self.AssignVbox.addWidget(self.ProjectNameInput)
        self.AssignVbox.addWidget(self.GuideToDeadLineSelection)
        self.AssignVbox.addWidget(self.SecondGuideToDeadlineSelection)
        self.AssignVbox.addWidget(self.ChosenDateAndTime)
        self.AssignVbox.addWidget(TaskAssignerSubmitButton)

        self.setLayout(self.AssignVbox)


if __name__ == '__main__':
    print('Program is Running!')
    app = QApplication(sys.argv)
    window = AssignTasksWindow()
    window.show()
    sys.exit(app.exec())
    print('Program is Running!')


"""print('Program is Running!')
>>>>>>> b353ea9844baeaa639631c3ea9944b86ab04550a
app = QApplication(sys.argv)
window = AssignWindow()
window.show()
sys.exit(app.exec())"""

#if __name__ == "__main__":
# app = QApplication(sys.argv)
# window = AssignWindow()
# window.show()
# sys.exit(app.exec())