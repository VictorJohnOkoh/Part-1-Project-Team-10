from cProfile import label
import random
import sys
from tkinter import font
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import (QApplication, QPushButton, QVBoxLayout, QWidget, 
                             QLabel, QScrollArea, QMainWindow, QSlider,
                             QLineEdit, QHBoxLayout, QWidget, QLineEdit)

#from profiling.tracing import label


testcase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

sentences = [
    "The sun dipped below the horizon, painting the sky orange and pink. A gentle breeze carried the scent of fresh flowers through the garden. The old library was filled with shelves of fascinating books.",
    "Rain tapped softly against the window throughout the afternoon. A curious squirrel darted between the trees in the park. The baker prepared warm loaves of bread before sunrise.",
    "Children laughed as they played games in the playground. The river flowed steadily toward the distant sea. A bright rainbow appeared after the storm had passed.",
    "The train arrived at the station exactly on time. Fresh snow covered the mountains in a blanket of white. The dog eagerly chased a ball across the field.",
    "A small café served delicious coffee and pastries. The artist carefully added the final details to the painting. Birds gathered on the roof as evening approached.",
    "The market was crowded with shoppers looking for bargains. A gardener watered the plants during the warm afternoon. The moon reflected brightly on the surface of the lake.",
    "Students worked together to complete their project. The cat curled up in a sunny spot near the window. A cyclist rode along the winding country road.",
    "The museum displayed artefacts from ancient civilizations. Leaves rustled quietly in the autumn wind. The chef experimented with a new recipe for dinner.",
    "A lighthouse stood proudly overlooking the coastline. The concert attracted visitors from many different towns. Early morning fog covered the fields and pathways.",
    "The football match kept fans excited until the final whistle. A photographer captured the beauty of the sunset. The campfire crackled gently beneath the starry night sky."
]



forum_replies = [
    [
        "",
        "",
        "Honestly, I would give it a try. You won't know whether you like it until you've actually experienced it.",
        "I was in exactly the same situation last year and decided to go for it. It turned out to be one of the best decisions I've made.",
        "If you're already thinking about it this much, that's probably a sign that you should give it a shot.",
        "I'd probably make a list of the pros and cons before deciding. Sometimes seeing everything written down makes the answer obvious.",
        "Personally, I wouldn't rush into it. Sleep on the decision for a few days and see if you still feel the same.",
    ],

    [
        "",
        "",
        "That sounds completely normal to me. Everyone struggles with this at some point.",
        "Don't be too hard on yourself. You're probably doing better than you think.",
        "I used to worry about exactly the same thing, but eventually I realised most people aren't judging you nearly as much as you imagine.",
        "Take things one step at a time rather than trying to solve everything at once.",
        "Sometimes the best thing you can do is take a break and come back to the problem with a clear head.",
    ],

    [
        "",
        "",
        "I'd definitely talk to them about it rather than letting it build up. Keeping everything bottled up usually makes things worse.",
        "Maybe start the conversation casually instead of making it into a huge serious discussion.",
        "If they're a good friend, they should be willing to listen even if they don't completely agree with you.",
        "I would be honest but try not to make it sound like you're blaming them for everything.",
        "You might be surprised by their reaction. They could have been thinking the exact same thing but were too nervous to mention it.",
    ],

    [
        "",
        "",
        "For me, the biggest improvement came from simply being consistent rather than trying to do everything perfectly.",
        "I'd recommend setting yourself a small target and increasing it gradually. Huge changes are difficult to maintain.",
        "Don't underestimate how much difference a good routine can make.",
        "I tried all the complicated methods first and eventually discovered that keeping things simple worked much better.",
        "Give it at least a few weeks before deciding whether it's working. Some changes take longer than you expect.",
    ],

    [
        "",
        "",
        "That sounds like a fantastic opportunity. I'd be tempted to say yes immediately.",
        "I'd consider the practical side first. Excitement is great, but make sure the numbers actually work.",
        "If this is something you've wanted for a long time, I wouldn't let a bit of uncertainty stop you.",
        "Ask yourself which decision you'd regret more in five years: doing it or not doing it?",
        "I'd speak to someone who's already done something similar before making the final decision.",
    ],

    [
        "",
        "",
        "I've had something almost identical happen to me. At the time it felt like a disaster, but eventually everything worked out.",
        "Sometimes things going wrong can actually lead you somewhere better than your original plan.",
        "Give yourself permission to be annoyed about it. You don't have to immediately turn every bad situation into a life lesson.",
        "I'd focus on what you can control rather than spending too much time thinking about what should have happened.",
        "It might not feel like it now, but this probably won't seem nearly as important a year from now.",
    ],

    [
        "",
        "",
        "I think you're overthinking it a little. Just ask them!",
        "The worst they can say is no, and at least then you'll know instead of wondering.",
        "I'd send a casual message rather than making a big announcement out of it.",
        "If you're worried about making things awkward, keep the first message simple and give them plenty of room to respond.",
        "Honestly, uncertainty is usually more uncomfortable than actually knowing the answer.",
    ],

    [
        "",
        "",
        "I've always preferred buying the cheaper option if it does basically the same job.",
        "In my experience, paying a little more for quality can save money in the long run.",
        "Check some independent reviews before buying anything. Marketing descriptions aren't always very helpful.",
        "I'd avoid making the decision purely based on price. Think about how often you'll actually use it.",
        "If you aren't sure, wait a week before buying it. If you still want it after that, it's probably worth considering.",
    ],

    [
        "",
        "",
        "This is one of those situations where there probably isn't a perfect answer.",
        "I'd choose the option that gives you the most flexibility. You can always change direction later.",
        "Have you considered trying both options on a small scale before committing completely?",
        "I'd ask a few people for opinions, but ultimately remember that you'll be the one living with the decision.",
        "Sometimes you just have to make the best decision you can with the information you have.",
    ],

    [
        "",
        "",
        "I completely understand why you're frustrated. That would annoy me too.",
        "I'd probably leave it alone for now and come back to it when you're less annoyed.",
        "Try not to respond while you're angry. Write what you want to say, wait an hour, then read it again.",
        "If it's something that can be fixed, focus on finding a solution rather than deciding who is responsible.",
        "Whatever you decide, don't let one bad experience convince you that everything will always turn out the same way."
    ]
]


class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        font = QFont()
        font.setPointSize(20)

        self.LeftWidget = QWidget()
        self.LeftVbox = QVBoxLayout()
        self.RightWidget = QWidget()
        self.RightVbox = QVBoxLayout()

        self.Hbox = QHBoxLayout()
    
        Labels = [] # for the body text, not the replies to the questions

        ReplyLabels = [] # for the replies to the questions, not the body text

        ButtonNames_Indexes = [] # for the buttons that are generated, and their indexes

        self.CurrentButtonIndex = 0

        def SubmitReplyButtonClicked():
        
                    forum_replies[self.CurrentButtonIndex].append(self.ReplyInput.text())
                    NewLabel_Replies = QLabel(text=self.ReplyInput.text())
                    self.RightVbox.addWidget(NewLabel_Replies)
                    NewLabel_Replies.hide()
                    ReplyLabels[self.CurrentButtonIndex].append(NewLabel_Replies)
                    #print(forum_replies[self.CurrentButtonIndex])
                    #print(ReplyLabels[self.CurrentButtonIndex])



        #Reply input and submit button
        self.ReplyInput = QLineEdit()
        self.ReplyInput.setFixedWidth(400)
        SubmitReplyButton = QPushButton(text='Submit Reply')
        SubmitReplyButton.setFixedSize(400,160)
        SubmitReplyButton.clicked.connect(SubmitReplyButtonClicked)
        self.RightVbox.addWidget(self.ReplyInput)
        self.RightVbox.addWidget(SubmitReplyButton)


        def Label_Management(CurrentLabel,CurrentReplyLabel,Labels,ReplyLabels):
            print(ReplyLabels)
            # For Questions in the Posts
            for i in range(0,len(Labels)):
                if Labels[i] != CurrentLabel:
                    Labels[i].hide()
                else:
                    Labels[i].show()

            # For the body in the Posts
            for j in range(0,len(ReplyLabels)):
                if ReplyLabels[j] != CurrentReplyLabel:
                    #ReplyLabels[j].hide()
                    for k in range(0,len(ReplyLabels[j])):
                        ReplyLabels[j][k].hide()
                else:
                    for kk in range(0,len(ReplyLabels[j])):
                        ReplyLabels[j][kk].show()


        def Button_Generator(PostTitles,self,font,PostTextBodies,PostReplies):
            Button_Numbers = []
            while len(Button_Numbers) != len(PostTitles):
                Temporary_Number = random.randrange(1, len(PostTitles) + 1)
                if str(Temporary_Number) not in Button_Numbers:
                    Button_Numbers.append(str(Temporary_Number))
            print(Button_Numbers)

            for b in range(0,len(Button_Numbers)):
                ButtonLabel_Post = QLabel(text=PostTextBodies[b])
                self.RightVbox.addWidget(ButtonLabel_Post)
                ButtonLabel_Post.hide()
                Labels.append(ButtonLabel_Post)
                #Label setup for the body of the text

                TempReplyLabelStorage = []
                for r in range(0,len(PostReplies[b])):
                    ReplyLabel = QLabel(text=PostReplies[b][r])
                    self.RightVbox.addWidget(ReplyLabel)
                    
                    ReplyLabel.hide()
                    TempReplyLabelStorage.append(ReplyLabel)
                ReplyLabels.append(TempReplyLabelStorage)



                ButtonName = Button_Numbers[b]
                ButtonNames_Indexes.append([ButtonName,b])
                ButtonName = QPushButton(text=ButtonName)
                ButtonName.setFixedSize(400,160)
                ButtonName.setFont(font)
                ButtonName.clicked.connect(lambda checked, z=b: setattr(self, 'CurrentButtonIndex', z))
                ButtonName.clicked.connect(lambda checked, z=ButtonLabel_Post, y=TempReplyLabelStorage: Label_Management(z,y,Labels,ReplyLabels))
                ButtonName.clicked.connect(self.ReplyInput.clear)
                self.LeftVbox.addWidget(ButtonName)       

        #Scrolling bit
        Button_Generator(testcase,self,font,sentences,forum_replies)
        self.LeftWidget.setLayout(self.LeftVbox)
        self.RightWidget.setLayout(self.RightVbox)
        scroll = QScrollArea(self)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        scroll.setWidget(self.LeftWidget)
        

        self.RightVbox.addStretch()
        self.Hbox.addWidget(scroll)
        self.Hbox.addWidget(self.RightWidget)
        self.setLayout(self.Hbox)


print('Program is Running!')
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())