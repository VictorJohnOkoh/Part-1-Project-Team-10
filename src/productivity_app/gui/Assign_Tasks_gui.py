#Assign Tasks
import random
import sys
from PyQt6.QtCore import QSize, Qt, QDateTime
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (QApplication, QPushButton, QVBoxLayout, QWidget, 
                             QLabel, QScrollArea, QMainWindow, QSlider,
                             QHBoxLayout, QLineEdit,QDateTimeEdit, QTextEdit)

class AssignWindow(QWidget):

    def DeadlineSelector_clicked(self):
                ChosenDeadline = self.ChosenDateAndTime.dateTime()
                ChosenDeadline_Formatted = ChosenDeadline.toString('dd-MM-yyyy HH:mm')
                Deadline = ChosenDeadline_Formatted
                print(Deadline)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.AssignWidget = QWidget()
        self.AssignVbox = QVBoxLayout()

        #Assign Button with Textboxes
        self.TaskNameInput = QLineEdit()
        self.TaskNameInput.setPlaceholderText('Name of task')
        self.TaskNameInput.setFixedWidth(400)

        self.TaskDescriptionInput = QTextEdit()
        self.TaskDescriptionInput.setPlaceholderText('Describe what needs to be done to finish the task')
        self.TaskDescriptionInput.setFixedWidth(400)
        self.TaskDescriptionInput.setFixedHeight(200)

        self.EmployeeNameInput = QLineEdit()
        self.EmployeeNameInput.setPlaceholderText('Employee Name')
        self.EmployeeNameInput.setFixedWidth(400)

        # setting up the deadline chooser for the managers/ team leaders
        self.Deadline = ''
            
        self.ChosenDateAndTime = QDateTimeEdit()
        self.ChosenDateAndTime.setCalendarPopup(True)
        self.ChosenDateAndTime.setDateTime(QDateTime.currentDateTime())

        DeadlineSelector = QPushButton(text='Choose Deadline')
        DeadlineSelector.setFixedSize(400,60)
        DeadlineSelector.clicked.connect(self.DeadlineSelector_clicked)


        self.AssignVbox.addWidget(self.TaskNameInput)
        self.AssignVbox.addWidget(self.TaskDescriptionInput)
        self.AssignVbox.addWidget(self.EmployeeNameInput)
        self.AssignVbox.addWidget(self.ChosenDateAndTime)
        self.AssignVbox.addWidget(DeadlineSelector)

        self.setLayout(self.AssignVbox)

print('Program is Running!')
app = QApplication(sys.argv)
window = AssignWindow()
window.show()
sys.exit(app.exec())

