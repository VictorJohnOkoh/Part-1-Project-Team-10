from productivity_app.users.Project import Project
from productivity_app.users.Employee import Employee
from productivity_app.users.TeamLead import Team_Leader

class Team:
    def __init__(self, project: Project, members: list[Employee], leader: Team_Leader):
        self.__project = project
        self.__members = members
        self.__leader = leader

    def get_leader(self) -> Team_Leader:
        return self.__leader

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
    
def parse_members(data: str) -> tuple[list, str]:
    mydict = dict((v.strip(), k.strip()) for k, v in (item.split(':') for item in data.split(',')))
    return list(mydict['member']), mydict['leader']
