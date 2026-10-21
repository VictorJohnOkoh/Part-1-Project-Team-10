from .Project import Project
from .Employee import Employee

class Team:
    def __init__(self, project: Project, members: list[Employee]):
        self.project = project
        self.members = members

    def add_member(self, member: Employee):
        self.members.append(member)

    def remove_member(self, member: Employee):
        self.members.remove(member)

    def get_members(self) -> list[Employee]:
        return self.members

    def get_project(self) -> Project:
        return self.project

    def get_members_count(self) -> int:
        return len(self.members)

