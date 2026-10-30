import random
import sys
from PyQt6.QtCore import QSize, Qt, QTimer, QDateTime
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import (QApplication, QPushButton, QVBoxLayout, QWidget, 
                             QLabel, QScrollArea, QMainWindow, QSlider,
                             QLineEdit, QHBoxLayout, QWidget, QLineEdit)
from productivity_app.gui import Assign_Tasks_gui

class ViewerForTasks(QWidget):

    #Tasks = Assign_Tasks_gui.AssignTasksWindow.GiveAssignments()
    # Tasks = [['Taking a big dump', 'Going to the toilet and wait for the chaos to begin', 'Jacob','Team 3', '31-10-2026 20:20',20,'Incomplete'],
    #          ['Making meal prep', 'Following the instructions, and putting in the ingredients', 'Jacob', 'Team 4', '03-11-2026 19:28',30,'Incomplete'],
    #            ['Going to Work', 'Getting in the car and driving straight there!', 'Jacob', 'Team 10', '28-10-2026 08:22',13,'Incomplete']]


    Tasks = [['Inspect Raw Materials', 'Check incoming raw materials for defects, damage and quality standards before approving them for production.', 'jake.peralta@make-it-all.co.uk', 'Team 1', '10-11-2026 08:30', 45, 'Incomplete'], 
              ['Machine Component Production', 'Operate CNC machinery to manufacture metal components according to the specified engineering drawings and measurements.', 'jake.peralta@make-it-all.co.uk', 'Team 2', '11-11-2026 09:00', 120, 'Incomplete'], 
              ['Assembly Line Preparation', 'Prepare the assembly workstation by organising tools, equipment and components required for the production run.', 'jake.peralta@make-it-all.co.uk', 'Team 3', '06-11-2026 07:40', 60, 'Incomplete'], 
              ['Quality Control Inspection', 'Inspect finished products for manufacturing defects, dimensional accuracy and compliance with company quality standards.', 'jake.peralta@make-it-all.co.uk', 'Team 4', '05-11-2026 06:00', 90, 'Incomplete'], 
              ['Equipment Maintenance', 'Carry out routine maintenance on manufacturing equipment, including lubrication, cleaning and checking mechanical components.', 'jake.peralta@make-it-all.co.uk', 'Team 5', '09-11-2026 08:00', 75, 'Incomplete'], 
              ['Packaging Finished Products', 'Package completed products using the correct protective materials and ensure all packages are labelled correctly.', 'jake.peralta@make-it-all.co.uk', 'Team 6', '10-11-2026 13:30', 60, 'Incomplete'], 
              ['Stock Inventory Update', 'Count available manufacturing components and update the inventory management system to reflect current stock levels.', 'jake.peralta@make-it-all.co.uk', 'Team 2', '12-11-2026 11:30', 45, 'Incomplete'], 
              ['Production Line Monitoring', 'Monitor the production line to ensure machinery is operating efficiently and production targets are being achieved.', 'jake.peralta@make-it-all.co.uk', 'Team 3', '16-11-2026 14:00', 180, 'Incomplete'], 
              ['Safety Equipment Inspection', 'Inspect workplace safety equipment, including emergency stops, protective guards and personal protective equipment.', 'jake.peralta@make-it-all.co.uk', 'Team 1', '06-11-2026 09:30', 60, 'Incomplete']]

    def __init__(self, parent=None):
        super().__init__(parent)

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
                TaskSeperator = QLabel(text='________________________________________________________________________________')
                NameOfTask = QLabel(text=GivenTask[0])
                DescOfTask = QLabel(text=GivenTask[1])
    
    
                DeadlineGiven_InDateTime = QDateTime.fromString(GivenTask[4], 'dd-MM-yyyy HH:mm')
                TimeToDeadline = QDateTime.currentDateTime().secsTo(DeadlineGiven_InDateTime)
                Months = TimeToDeadline // 2419200
                MonthsRemainder = TimeToDeadline % 2419200
                Days = MonthsRemainder // 86400
                DaysRemainder = MonthsRemainder % 86400
                Hours = (DaysRemainder // 3600)
                HoursRemainder = DaysRemainder % 3600
                Minutes = HoursRemainder // 60
                RemainingDeadline = QLabel(text=str(Months) + ' Months ' + str(Days) + ' Days ' + str(Hours) + ' Hours ' + str(Minutes) + ' Minutes')            
    
                DeadlineLabels.append([RemainingDeadline,GivenTask[4]])

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
                    GivenTask[6] = Button.TaskStatus
                    print(GivenTask)

                        
                
                ActionButton.clicked.connect(lambda checked, b = ActionButton, t = RemainingTime: ActionButton_clicked(b,t))
    
                SlotWidget = QWidget()
                Slot = QVBoxLayout()
                Slot.addWidget(NameOfTask)
                Slot.addWidget(DescOfTask)
                Slot.addWidget(RemainingDeadline)
                Slot.addWidget(ActionButton)
                Slot.addWidget(TaskSeperator)
                SlotWidget.setLayout(Slot)
                SlotContainers.append(SlotWidget)

        self.ClockTimer = QTimer()
        self.ClockTimer.start(60000)
        self.ClockTimer.timeout.connect(lambda l = DeadlineLabels: Update_Deadlines(l))



        #Scrolling bit
        TaskDisplayer('jake.peralta@make-it-all.co.uk',self.Tasks)
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
        scroll.setMinimumSize(1800,900)

if __name__ == '__main__':
    print('Program is Running!')
    app = QApplication(sys.argv)
    Viewer = ViewerForTasks()
    Viewer.show()
    sys.exit(app.exec())