import datetime
from User import User

class Project:
    def __init__(self, name,date: type[datetime], goal: str,team_members: list[User] = None):
        self.name = name
        self.date = date
        self.team_members = team_members
        self.goal = goal

    def get_project_name(self) -> str:
        return self.name

    def assign_member(self, new_member: User) -> None:
        self.team_members.append(new_member)

    def remove_member(self, member: User) -> None:
        self.team_members.remove(member)

    def get_team_members(self) -> list[User]:
        return self.team_members

    def get_project_goal(self) -> str:
        return self.goal

    def change_project_goal(self, new_goal) -> None:
        self.goal = new_goal