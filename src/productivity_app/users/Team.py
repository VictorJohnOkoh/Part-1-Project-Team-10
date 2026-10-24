from .Project import Project
from .Employee import Employee

class Team:
    def __init__(self, project: Project, members: list[Employee]):
        self.__project = project
        self.__members = members

    def add_member(self, member: Employee) -> None:
        self.__members.append(member)

    def remove_member(self, member: Employee) -> None:
        self.__members.remove(member)

    def get_members(self) -> list[Employee]:
        return self.__members

    def get_project(self) -> Project:
        return self.__project

    def get_members_count(self) -> int:
        return len(self.__members)

