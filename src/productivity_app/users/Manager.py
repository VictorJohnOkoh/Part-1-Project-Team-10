from User import User
from Project import Project

class Manager(User):
    def __init__(self, id: int, first_name: str, last_name: str, email: str, projects: list[Project]|None = None):
        super().__init__(id, first_name, last_name, email, tasks=projects)
