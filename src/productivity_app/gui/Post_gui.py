import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import (QApplication, QPushButton, QVBoxLayout, QWidget, 
                             QLabel, QScrollArea, QMainWindow, QSlider,
                             QLineEdit, QHBoxLayout, QGridLayout, QTextEdit, QComboBox, QDialog, QMessageBox)
from productivity_app.services.Post_Functions import post, create_post, make_comment, RestrictedTopics, view_post, make_post, RestrictTopics
from ..users.Manager import Manager

#from profiling.tracing import label

class PostWindow(QWidget):

    Labels = [] # for the body text, not the replies to the questions
    PostButtons = []

    def Label_Management(self,CurrentLabel,Labels, current_topic, current_title):
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
            if topics not in RestrictedTopics:
                posts_found = post[topics]
                for single_posts in posts_found:
                    ButtonName = single_posts["title"]
                    ButtonLabel_Post = QLabel(text=single_posts["body"])
                    self.RightVbox.addWidget(ButtonLabel_Post)
                    ButtonLabel_Post.hide()
                    self.Labels.append(ButtonLabel_Post)

                    #TempReplyLabelStorage = comment_finder(self, single_posts["comments"], ReplyLabels)
                    ButtonName = QPushButton(text=ButtonName)
                    ButtonName.setFixedSize(400,160)
                    ButtonName.setFont(font)

                    ButtonName.clicked.connect(lambda checked, z=ButtonLabel_Post, t=topics, title=single_posts["title"]: (
                        setattr(self, 'current_topic', t),
                        setattr(self, 'current_title', title),
                        setattr(self, 'current_body_label', z),
                        self.Label_Management(z, self.Labels, t, title)
                    ))
                    ButtonName.clicked.connect(self.ReplyInput.clear)
                    self.LeftVbox.addWidget(ButtonName) 

                    self.PostButtons.append({'widget': ButtonName, 'topic': topics}) 

    def Create_New_Post(self):
        Message = QMessageBox()
        Add_New_Post_Window = QDialog(self)
        Add_New_Post_Window.setFixedSize(430,250)
        Add_New_Post_Window_Layout = QVBoxLayout(Add_New_Post_Window)


        def SubmitNewPost():
            font = QFont()
            font.setPointSize(20)

            Topic = self.TopicInput.text().strip().lower()
            if Topic in RestrictedTopics:
                Message.setFixedSize(300, 100)
                Message.setText("Topic is restricted")
                Message.setInformativeText("Please choose a different topic")
                Message.setIcon(QMessageBox.Icon.Information)
                Message.exec()

                self.TopicInput.clear()
                self.TitleInput.clear()
                self.BodyInput.clear()
                return

            Title = self.TitleInput.text().strip().lower()
            Body = self.BodyInput.toPlainText().strip().lower()

            if not Topic or not Title or not Body:
                print("Please type valid inputs")
                return

            make_post(Topic, Title, Body)
            self.SearchInput.addItem(Topic)
            self.RestrictedTextBox.addItem(Topic)

            self.TopicInput.clear()
            self.TitleInput.clear()
            self.BodyInput.clear()

            ButtonLabel_Post = QLabel(text=Body)
            self.RightVbox.insertWidget(8, ButtonLabel_Post)
            ButtonLabel_Post.hide()
            self.Labels.append(ButtonLabel_Post)

            ButtonName = QPushButton(text=Title)
            ButtonName.setFixedSize(400, 160)
            ButtonName.setFont(font)

            ButtonName.clicked.connect(lambda checked, z=ButtonLabel_Post, t=Topic, title=Title: (
                setattr(self, 'current_topic', t),
                setattr(self, 'current_title', title),
                setattr(self, 'current_body_label', z),
                self.Label_Management(z, self.Labels, t, title)
            ))
            #ButtonName.clicked.connect(self.ReplyInput.clear)

            self.LeftVbox.addWidget(ButtonName)
            self.PostButtons.append({'widget': ButtonName, 'topic': Topic})
            Add_New_Post_Window.accept()

        self.TopicInput = QLineEdit()
        self.TopicInput.setPlaceholderText('Enter topic here')
        self.TitleInput = QLineEdit()
        self.TitleInput.setPlaceholderText('Enter title here')
        self.BodyInput = QTextEdit()
        self.BodyInput.setPlaceholderText('Describe the problem here')
        self.TopicInput.setFixedWidth(400)
        self.TitleInput.setFixedWidth(400)
        self.BodyInput.setFixedSize(400,80)
        SubmitPostButton = QPushButton(text='Make new post')
        SubmitPostButton.setFixedSize(400,40)
        Add_New_Post_Window_Layout.addWidget(self.TopicInput)
        Add_New_Post_Window_Layout.addWidget(self.TitleInput)
        Add_New_Post_Window_Layout.addWidget(self.BodyInput)
        Add_New_Post_Window_Layout.addWidget(SubmitPostButton)
        SubmitPostButton.clicked.connect(SubmitNewPost)
        Add_New_Post_Window.exec()

    def __init__(self, user, parent=None):
        super().__init__(parent)
        self.setWindowTitle("MAKE IT ALL - Forum Posts")
        font = QFont()
        font.setPointSize(20)
        self.user = user
        
    
        self.LeftWidget = QWidget()
        self.LeftVbox = QVBoxLayout()
        self.RightWidget = QWidget()
        self.RightVbox = QVBoxLayout()

        self.Hbox = QHBoxLayout()
    
        # Labels = [] # for the body text, not the replies to the questions
        # PostButtons = []

        def SearchPost():
            Message = QMessageBox()
            Topic = self.SearchInput.currentText()
            strtopic = Topic.strip().lower()

            for item in self.PostButtons:
                if strtopic not in RestrictedTopics and item['topic'] not in RestrictedTopics:
                    if not strtopic:
                        item['widget'].show()
                    elif item['topic'].lower() == strtopic:
                        item['widget'].show()
                    else:
                        item['widget'].hide()
                elif strtopic in RestrictedTopics and strtopic != "":
                    Message.setFixedSize(300, 100)
                    Message.setText("Topic is restricted")
                    Message.setInformativeText("Please search for a different topic")
                    Message.setIcon(QMessageBox.Icon.Information)
                    Message.exec()
                    return


        self.SearchInput = QComboBox()
        post_topics_combobox = post.keys()
        self.SearchInput.addItem('')
        for topic in post_topics_combobox:
            self.SearchInput.addItem(topic)
        self.SearchInput.setFixedWidth(400)
        SubmitSearchButton = QPushButton(text='Search by topic')
        SubmitSearchButton.setFixedSize(400,40)
        SubmitSearchButton.clicked.connect(SearchPost)
        self.RightVbox.addWidget(self.SearchInput)
        self.RightVbox.addWidget(SubmitSearchButton)

        self.CurrentButtonIndex = 0

        def SubmitReplyButtonClicked():
            Message = QMessageBox()
            comment_text = self.ReplyInput.text()
            if not comment_text.strip():
                return

            if not hasattr(self, 'current_topic') or not hasattr(self, 'current_title'):
                Message.setFixedSize(300, 100)
                Message.setText("No Post selected")
                Message.setInformativeText("Please click on a post to comment")
                Message.setIcon(QMessageBox.Icon.Information)
                Message.exec()
                return

            if not self.current_topic or not self.current_title:
                return

            if self.current_topic in RestrictedTopics:
                Message.setFixedSize(300, 100)
                Message.setText("Post is restricted")
                Message.setInformativeText("Please comment on another post")
                Message.setIcon(QMessageBox.Icon.Information)
                Message.exec()

            make_comment(self.current_topic, self.current_title, comment_text)
            self.ReplyInput.clear()

            if hasattr(self, 'current_body_label') and self.current_body_label:
                self.Label_Management(self.current_body_label, self.Labels, self.current_topic, self.current_title)

        def RestrictTopicButtonClicked():
            InpRestrictedTopics = self.RestrictedTextBox.currentText()
            RestrictTopics(InpRestrictedTopics)

            strRestrictedTopic = InpRestrictedTopics.strip().lower()

            for item in self.PostButtons:
                if item["topic"].lower() == strRestrictedTopic:
                    item["widget"].hide()


        self.RestrictedTextBox = QComboBox()
        restricted_topics_combobox = post.keys()
        for topic in restricted_topics_combobox:
            self.RestrictedTextBox.addItem(topic)
        self.RestrictedTextBox.setPlaceholderText('Enter restricted topic here')
        self.RestrictedTextBox.setFixedWidth(400)
        RestrictedTopicsButton = QPushButton(text='Submit Restricted Topic')
        RestrictedTopicsButton.setFixedSize(400,40)
        RestrictedTopicsButton.clicked.connect(RestrictTopicButtonClicked)

        if isinstance(self.user, Manager):
            self.RightVbox.addWidget(self.RestrictedTextBox)
            self.RightVbox.addWidget(RestrictedTopicsButton)          
        
        self.ReplyInput = QLineEdit()
        self.ReplyInput.setPlaceholderText('Enter your comment here')
        self.ReplyInput.setFixedWidth(400)
        SubmitReplyButton = QPushButton(text='Post Comment')
        SubmitReplyButton.setFixedSize(400,40)
        SubmitReplyButton.clicked.connect(SubmitReplyButtonClicked)
        self.RightVbox.addWidget(self.ReplyInput)
        self.RightVbox.addWidget(SubmitReplyButton)


        CreateNewPostButton = QPushButton('New Post')
        CreateNewPostButton.setFixedSize(400,80)
        CreateNewPostButton.clicked.connect(self.Create_New_Post)
        self.RightVbox.addWidget(CreateNewPostButton)





        #Scrolling bit
        self.Button_Generator(font)
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