import random
import sys
from PyQt6.QtCore import QSize, Qt, QTimer, QDateTime
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import (QApplication, QPushButton, QVBoxLayout, QWidget, 
                             QLabel, QScrollArea, QMainWindow, QSlider,
                             QLineEdit, QHBoxLayout, QWidget, QLineEdit)

class ViewerForTasks(QWidget):
    
    Tasks = [['Taking a big dump', 'Going to the toilet and wait for the chaos to begin', 'Jacob', '31-10-2026 20:20',20,'Incomplete'],
              ['Making meal prep', 'Following the instructions, and putting in the ingredients', 'Jacob', '03-11-2026 19:28',30,'Incomplete'],
                ['Going to Work', 'Getting in the car and driving straight there!', 'Jacob', '28-10-2026 08:22',13,'Incomplete']]

    def __init__(self, parent=None):
        super().__init__(parent)
        # ClockTimer = QTimer()
        # ClockTimer.start(60000)
        # ClockTimer.timeout.connect(Update_Deadlines())

        SlotContainers = []

        DeadlineLabels = []
        def DeadlineCreation(DeadlineGiven,LabelGiven):
            DeadlineGiven_InDateTime = QDateTime.fromString(DeadlineGiven, 'dd-MM-yyyy HH:mm')
            TimeToDeadline = QDateTime.currentDateTime().secsTo(DeadlineGiven_InDateTime)
            Months = TimeToDeadline // 2419200
            MonthsRemainder = TimeToDeadline % 2419200
            Days = MonthsRemainder // 86400
            DaysRemainder = MonthsRemainder % 86400
            Hours = (DaysRemainder // 3600)
            HoursRemainder = DaysRemainder % 3600
            Minutes = HoursRemainder // 60
            LabelGiven.setText(str(Months) + ' Months ' + str(Days) + ' Days ' + str(Hours) + ' Hours ' + str(Minutes) + ' Minutes')
            return LabelGiven

        def Update_Deadlines(Deadline_Labels):
            print('Entered Update_Deadlines()')
            for Label, Deadline in Deadline_Labels:
                DeadlineCreation(Deadline,Label)
                print('Deadlines Updated!')
            return Deadline_Labels

    
        def TaskDisplayer(Username,AssignedTasks):
    
            SuitableTasks = []
    
            for task in AssignedTasks:
                if task[2] == Username:
                    SuitableTasks.append(task)
                    print('Going through tasks...')
    
            for GivenTask in SuitableTasks:
                NameOfTask = QLabel(text=GivenTask[0])
                DescOfTask = QLabel(text=GivenTask[1])
    
    
                DeadlineGiven_InDateTime = QDateTime.fromString(GivenTask[3], 'dd-MM-yyyy HH:mm')
                TimeToDeadline = QDateTime.currentDateTime().secsTo(DeadlineGiven_InDateTime)
                Months = TimeToDeadline // 2419200
                MonthsRemainder = TimeToDeadline % 2419200
                Days = MonthsRemainder // 86400
                DaysRemainder = MonthsRemainder % 86400
                Hours = (DaysRemainder // 3600)
                HoursRemainder = DaysRemainder % 3600
                Minutes = HoursRemainder // 60
                RemainingDeadline = QLabel(text=str(Months) + ' Months ' + str(Days) + ' Days ' + str(Hours) + ' Hours ' + str(Minutes) + ' Minutes')            
    
                DeadlineLabels.append([RemainingDeadline,GivenTask[3]])

                ActionButton = QPushButton(text='Start Task')
                ActionButton.setFixedSize(400,60)

                
    
                ActionButton.TaskStatus = 'Incomplete'
                RemainingTime = RemainingDeadline.text()

                def ActionButton_clicked(Button, TimeText):
                    if Button.TaskStatus == 'Incomplete':
                        Button.TaskStatus = 'In progress'
                        Button.setText('Finish')
                    elif Button.TaskStatus == 'In progress':
                        Button.TaskStatus = 'Complete'
                        if TimeText ==  '0 Months 0 Days 0 Hours 0 Minutes':
                            Button.TaskStatus = 'Finished Late'
                    GivenTask[5] = Button.TaskStatus
                    print(GivenTask)

                        
                
                ActionButton.clicked.connect(lambda checked, b = ActionButton, t = RemainingTime: ActionButton_clicked(b,t))
    
                SlotWidget = QWidget()
                Slot = QVBoxLayout()
                Slot.addWidget(NameOfTask)
                Slot.addWidget(DescOfTask)
                Slot.addWidget(RemainingDeadline)
                Slot.addWidget(ActionButton)
                SlotWidget.setLayout(Slot)
                SlotContainers.append(SlotWidget)

        self.ClockTimer = QTimer()
        self.ClockTimer.start(60000)
        self.ClockTimer.timeout.connect(lambda l = DeadlineLabels: Update_Deadlines(l))



        #Scrolling bit
        TaskDisplayer('Jacob',self.Tasks)
        self.AllWidgets = QWidget()
        self.AllWidgetsVbox = QVBoxLayout()
        for container in SlotContainers:
            self.AllWidgetsVbox.addWidget(container)
        self.AllWidgets.setLayout(self.AllWidgetsVbox)
        scroll = QScrollArea(self)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        scroll.setWidget(self.AllWidgets)
        scroll.setMinimumSize(450,400)

print('Program is Running!')
app = QApplication(sys.argv)
Viewer = ViewerForTasks()
Viewer.show()
sys.exit(app.exec())