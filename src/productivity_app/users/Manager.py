from .Employee import Employee
from .Project import Project
from datetime import datetime

class Manager(Employee):
    def __init__(self, id: int, first_name: str, last_name: str, email: str, projects: list[Project]|None = None):
        super().__init__(id, first_name, last_name, email, tasks=projects)

    def create_new_project(self, name: str, goal: str, deadline: type[datetime]=None):
        new_project = Project(name, datetime.datetime.now(), goal, deadline)
        self.tasks.append(new_project)

    def get_employee_details(self, employee: Employee):
        return employee.id, employee.get_full_name(), employee.email, employee.tasks