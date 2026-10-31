import re
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel,QPushButton,
    QLineEdit,QVBoxLayout,QGridLayout,
    QMessageBox
    
    )
from datetime import datetime
from pathlib import Path
from productivity_app.services.hashing_function import verify_password, hash_password

"""
The test_users.txt is just to test the functionality of the password verification
The data is subject to change as required
"""

def tracker(username,password):
    TRACKER_FILE = Path(__file__).parent.parent / "services" / "invalid_attempts.txt"
    timestamp = datetime.now().isoformat(timespec = "seconds").replace(":","-") 
    with open(TRACKER_FILE,"a") as tracking_file:
        tracking_file.write(f"{username}:{password}:{timestamp}\n")

#function used to check if the username and password exist in the file
def check_credentials(username,password):
    USERS_FILE = Path(__file__).parent.parent / "users" / "valid_users.txt"
    with open(USERS_FILE,"r") as user_file:
        for line in user_file:
            current_line = line.strip().split(":")
            if current_line[0] == username and verify_password(password,current_line[1]):
                #only returns the role if the credentials exist in the file
                return current_line[2]
            elif current_line[0] == username and not verify_password(password,current_line[1]):
                return None

def get_authorised(email):
    authorised_file = Path(__file__).parent.parent / "users" / "authorised_users.txt"
    with open (authorised_file,"r") as authorised:
        for line in authorised:
            parts = line.strip().split(":")
            if len(parts) == 3 and parts[0].lower() == email:
                return parts[2]
    return None

def user_exist(email):
    USERS_FILE = Path(__file__).parent.parent / "users" / "valid_users.txt"
    with open(USERS_FILE, "r") as f:
        for line in f:
            if line.strip().split(":")[0].lower() == email.lower():
                return True
    return False

def add_user(username,password,role):
    hashed = hash_password(password)
    USERS_FILE = Path(__file__).parent.parent / "users" / "valid_users.txt"
    with open(USERS_FILE,"a") as f:
        f.write(f"{username}:{hashed}:{role}\n")

#used to check if the username is correct
def check_user(username: str, password: str):
    if re.search(r"^[^@\s]+@make-it-all\.co\.uk$",username):

        #call function to hash password entered
        role = check_credentials(username,password) 
        if role == "team_leader":
            return "team_leader"
            #function to take the user to admin screen
        elif role =="team_member":
            #print("You will be taken to the team member screen")
            #function to take user to team member screen
            return "team_member"
        elif role == "manager":
            return 'manager'
        else:
            tracker(username,password)
            return "unauth_user"
    else:
        tracker(username,password)
        return "unauth_user"

#test use cases
#check_user("john.smith@make-it-all.co.uk","hash")
#check_user("Fake credentials")

tracker("username1","password1")
