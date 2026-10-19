from __future__ import annotations
from typing import TYPE_CHECKING
import datetime

if TYPE_CHECKING:
    from src.productivity_app.users.Employee import Employee

class Project:
    def __init__(self, name, date: type[datetime], goal: str, team_members: list[Employee] = None, deadline: type[datetime] = None):
        self.name = name
        self.date = date
        self.team_members = team_members
        self.goal = goal
        self.deadline = deadline

    def get_project_name(self) -> str:
        return self.name

    def assign_member(self, new_member: Employee) -> None:
        self.team_members.append(new_member)

    def remove_member(self, member: Employee) -> None:
        self.team_members.remove(member)

    def get_team_members(self) -> list[Employee]:
        return self.team_members

    def get_project_goal(self) -> str:
        return self.goal

    def change_project_goal(self, new_goal) -> None:
        self.goal = new_goal

    def get_project_deadline(self):
        return self.deadline