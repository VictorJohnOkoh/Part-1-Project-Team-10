from __future__ import annotations
from typing import TYPE_CHECKING
import datetime


class Project:
    def __init__(self, name, date: type[datetime], goal: str = None, deadline: type[datetime] = None):
        self.name = name
        self.date = date
        self.goal = goal
        self.deadline = deadline

    def get_project_name(self) -> str:
        return self.name

    def get_project_goal(self) -> str | None:
        return self.goal

    def change_project_goal(self, new_goal) -> None:
        self.goal = new_goal

    def get_project_deadline(self):
        return self.deadline