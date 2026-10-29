from .Employee import Employee
from .Project import Project
from datetime import datetime

# Managers can view and create projects company wide, as well as view wmployee details. 
# a manager is also an employee, so they inherit the properties of an employee.
# Managers don't have tasks 

class Manager(Employee):
    def __init__(self, id: int, first_name: str, last_name: str, email: str, projects: list[Project]|None = None):
        super().__init__(id, first_name, last_name, email, tasks=[])
        self.__projects = projects if projects is not None else []
    
    def view_projects(self) -> list[Project]:
        return self.__projects

    def create_new_project(self, name: str, goal: str, deadline: datetime | None=None):
        new_project = Project(name, datetime.now(), goal, deadline)
        self.__projects.append(new_project)

    def get_employee_details(self, employee: Employee):
        return employee.get_id(), employee.get_full_name(), employee.get_email(), employee.get_tasks()
    
    def get_role(self) -> str:
        return 'Manager'

    def __str__(self) -> str:
        return super().__str__()
    
manager1 = Manager(4444, 'Anakin', 'Skywaler', 'anakin.skywalker@make-it-all.co.uk')