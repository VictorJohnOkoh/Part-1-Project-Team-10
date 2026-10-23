#Assign Tasks
import random
import sys
from PyQt6.QtCore import QSize, Qt, QDateTime
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (QApplication, QPushButton, QVBoxLayout, QWidget, 
                             QLabel, QScrollArea, QMainWindow, QSlider,
                             QHBoxLayout, QLineEdit,QDateTimeEdit)

class AssignWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.AssignWidget = QWidget()
        self.AssignVbox = QVBoxLayout()

        #Assign Button with Textboxes
        self.TaskNameInput = QLineEdit()
        self.TaskNameInput.setFixedWidth(400)

        self.TaskDescriptionInput = QLineEdit()
        self.TaskDescriptionInput.setFixedWidth(400)

        self.EmployeeNameInput = QLineEdit()
        self.EmployeeNameInput.setFixedWidth(400)

        # setting up the deadline chooser for the managers/ team leaders
        Deadline = ''
            
        self.ChosenDateAndTime = QDateTimeEdit()
        self.ChosenDateAndTime.setCalendarPopup(True)

        def DeadlineSelector_clicked(self):
            ChosenDeadline = self.ChosenDateAndTime.dateTime()
            ChosenDeadline_Formatted = ChosenDeadline.toString('dd-MM-yyyy HH:mm')
            Deadline = ChosenDeadline_Formatted
            

        DeadlineSelector = QPushButton(text='Choose Deadline')
        DeadlineSelector.setFixedSize(400,160)
        DeadlineSelector.clicked.connect(DeadlineSelector_clicked)


        self.AssignVbox.addWidget(self.TaskNameInput)
        self.AssignVbox.addWidget(self.TaskDescriptionInput)
        self.AssignVbox.addWidget(self.EmployeeNameInput)
        self.AssignVbox.addWidget(self.ChosenDateAndTime)
        self.AssignVbox.addWidget(DeadlineSelector)


        if len(Deadline) != 0:
            print(Deadline)

        self.setLayout(self.AssignVbox)

print('Program is Running!')
app = QApplication(sys.argv)
window = AssignWindow()
window.show()
sys.exit(app.exec())