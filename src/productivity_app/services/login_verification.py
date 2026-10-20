import re
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel,QPushButton,
    QLineEdit,QVBoxLayout,QGridLayout,
    QMessageBox
    
    )
from pathlib import Path
from productivity_app.services.hashing_function import verify_password

"""
The test_users.txt is just to test the functionality of the password verification
The data is subject to change as required
"""


#function used to check if the username and password exist in the file
def check_credentials(username,password):
    USERS_FILE = Path(__file__).parent.parent / "users" / "test_users.txt"
    with open(USERS_FILE,"r") as user_file:
        for line in user_file:
            current_line = line.strip().split(":")
            if current_line[0] == username and verify_password(password,current_line[1]):
                #only returns the role if the credentials exist in the file
                return current_line[2]
            elif current_line[0] == username and current_line[1] != password:
                return None



#used to check if the username is correct
def check_user(username: str, password: str):
    if re.search("@make-it-all.co.uk",username):

        #call function to hash password entered
        role = check_credentials(username,password) 
        if role == "team_leader":
            return "team_leader"
            #function to take the user to admin screen
        elif role =="team_member":
            #print("You will be taken to the team member screen")
            #function to take user to team member screen
            return "team_member"
        else:
            #call function to log invalid login attempt
            return "unauth_user"
    else:
        #call function to log invalid login attempt
        return "unauth_user"

#test use cases
#check_user("john.smith@make-it-all.co.uk","hash")
#check_user("Fake credentials")