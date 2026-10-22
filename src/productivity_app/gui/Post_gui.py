
import random
import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import (QApplication, QPushButton, QVBoxLayout, QWidget, 
                             QLabel, QScrollArea, QMainWindow, QSlider,
                             QLineEdit, QHBoxLayout, QWidget, QLineEdit)
from productivity_app.services.Post_Functions import post, create_post, make_comment, RestrictedTopics, view_post, make_post
#from profiling.tracing import label

class PostWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("MAKE IT ALL - Forum Posts")
        font = QFont()
        font.setPointSize(20)

    
        self.LeftWidget = QWidget()
        self.LeftVbox = QVBoxLayout()
        self.RightWidget = QWidget()
        self.RightVbox = QVBoxLayout()

        self.Hbox = QHBoxLayout()
    
        Labels = [] # for the body text, not the replies to the questions
        PostButtons = []
        ReplyLabels = [] # for the replies to the questions, not the body text

        ButtonNames_Indexes = [] # for the buttons that are generated, and their indexes

        self.CurrentButtonIndex = 0

        def SubmitReplyButtonClicked():
            comment_text = self.ReplyInput.text()
            if not comment_text.strip():
                return

            if not self.current_topic or not self.current_title:
                return

            make_comment(self.current_topic, self.current_title, comment_text)
            self.ReplyInput.clear()

            if hasattr(self, 'current_body_label') and self.current_body_label:
                Label_Management(self.current_body_label, Labels, self.current_topic, self.current_title)

        def SearchPost():
            Topic = self.SearchInput.text()
            strtopic = Topic.strip().lower()

            for item in PostButtons:
                if not strtopic:
                    item['widget'].show()
                elif item['topic'].lower() == strtopic:
                    item['widget'].show()
                else:
                    item['widget'].hide()

        def SubmitNewPost():
            Topic = self.TopicInput.text().strip().lower()
            Title = self.TitleInput.text().strip().lower()
            Body = self.BodyInput.text().strip().lower()

            if not Topic or not Title or not Body:
                print("Please type valid inputs")
                return

            make_post(Topic, Title, Body)

            self.TopicInput.clear()
            self.TitleInput.clear()
            self.BodyInput.clear()

            ButtonLabel_Post = QLabel(text=Body)
            self.RightVbox.addWidget(ButtonLabel_Post)
            ButtonLabel_Post.hide()
            Labels.append(ButtonLabel_Post)

            ButtonName = QPushButton(text=Title)
            ButtonName.setFixedSize(400, 160)
            ButtonName.setFont(font)

            ButtonName.clicked.connect(lambda checked, z=ButtonLabel_Post, t=Topic, title=Title: (
                setattr(self, 'current_topic', t),
                setattr(self, 'current_title', title),
                setattr(self, 'current_body_label', z),
                Label_Management(z, Labels, t, title)
            ))
            ButtonName.clicked.connect(self.ReplyInput.clear)

            self.LeftVbox.addWidget(ButtonName)
            PostButtons.append({'widget': ButtonName, 'topic': Topic})
            


        #Reply input and submit button
        self.ReplyInput = QLineEdit()
        self.ReplyInput.setFixedWidth(400)
        SubmitReplyButton = QPushButton(text='Post Comment')
        SubmitReplyButton.setFixedSize(400,160)
        SubmitReplyButton.clicked.connect(SubmitReplyButtonClicked)
        self.RightVbox.addWidget(self.ReplyInput)
        self.RightVbox.addWidget(SubmitReplyButton)

        self.SearchInput = QLineEdit()
        self.SearchInput.setFixedWidth(400)
        SubmitSearchButton = QPushButton(text='Search by topic')
        SubmitSearchButton.setFixedSize(400,160)
        SubmitSearchButton.clicked.connect(SearchPost)
        self.RightVbox.addWidget(self.SearchInput)
        self.RightVbox.addWidget(SubmitSearchButton)

        self.TopicInput = QLineEdit()
        self.TitleInput = QLineEdit()
        self.BodyInput = QLineEdit()
        self.TopicInput.setFixedWidth(400)
        self.TitleInput.setFixedWidth(400)
        self.BodyInput.setFixedWidth(400)
        SubmitPostButton = QPushButton(text='Make new post')
        SubmitPostButton.setFixedSize(400,160)
        SubmitPostButton.clicked.connect(SubmitNewPost)
        self.RightVbox.addWidget(self.TopicInput)
        self.RightVbox.addWidget(self.TitleInput)
        self.RightVbox.addWidget(self.BodyInput)
        self.RightVbox.addWidget(SubmitPostButton)
            
            

        def Label_Management(CurrentLabel,Labels, current_topic, current_title):
            # For Questions in the Posts
            for i in range(0,len(Labels)):
                Labels[i].hide()
                if Labels[i] != CurrentLabel:
                    Labels[i].hide()
                else:
                    Labels[i].show()

            if hasattr(self, 'active_comment_labels') and self.active_comment_labels:
                for lbl in self.active_comment_labels:
                    self.RightVbox.removeWidget(lbl)
                    lbl.deleteLater()

            self.active_comment_labels = []
            target_comments = []
            if current_topic in post:
                for single_post in post[current_topic]:
                    if single_post["title"] == current_title:
                        target_comments = single_post["comments"]
                        break

            for comments in target_comments:
                commentLabels = QLabel(text=comments)

                input_index = self.RightVbox.indexOf(self.ReplyInput)
                self.RightVbox.addWidget(commentLabels)

                commentLabels.show()

                self.active_comment_labels.append(commentLabels)


        def Button_Generator(self,font):
            for topics in post.keys():
                posts_found = post[topics]
                for single_posts in posts_found:
                    ButtonName = single_posts["title"]
                    ButtonLabel_Post = QLabel(text=single_posts["body"])
                    self.RightVbox.addWidget(ButtonLabel_Post)
                    ButtonLabel_Post.hide()
                    Labels.append(ButtonLabel_Post)

                    #TempReplyLabelStorage = comment_finder(self, single_posts["comments"], ReplyLabels)
                    ButtonName = QPushButton(text=ButtonName)
                    ButtonName.setFixedSize(400,160)
                    ButtonName.setFont(font)

                    ButtonName.clicked.connect(lambda checked, z=ButtonLabel_Post, t=topics, title=single_posts["title"]: (
                        setattr(self, 'current_topic', t),
                        setattr(self, 'current_title', title),
                        setattr(self, 'current_body_label', z),
                        Label_Management(z, Labels, t, title)
                    ))
                    ButtonName.clicked.connect(self.ReplyInput.clear)
                    self.LeftVbox.addWidget(ButtonName) 

                    PostButtons.append({'widget': ButtonName, 'topic': topics}) 


        #Scrolling bit
        Button_Generator(self,font)
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PostWindow()
    window.show()
    sys.exit(app.exec())