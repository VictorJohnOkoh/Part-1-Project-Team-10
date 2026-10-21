from enum import Enum

class LoginVerification(Enum):
    MANAGER = "manager"
    MEMBER = "member"

def check_user(username: str) -> LoginVerification | None:
    if username == "admin":
        return LoginVerification.MANAGER
    elif username == "member":
        return LoginVerification.MEMBER
    return None

def check_password(password: str):
    if password == "admin":
        return LoginVerification.MANAGER
    elif password == "member":
        return LoginVerification.MEMBER
    return None