from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import datetime


class Project:
    def __init__(self, name, date: datetime, goal: str | None = None, deadline: datetime | None = None):
        self.name = name
        self.date = date
        self.goal = goal
        self.deadline = deadline

    def get_project_name(self) -> str:
        return self.name

    def get_project_goal(self) -> str | None:
        return self.goal

    def change_project_goal(self, new_goal: str | None) -> None:
        self.goal = new_goal

    def get_project_deadline(self) -> datetime | None:
        return self.deadline

proj1 = Project('Example', datetime(day=25, month=1, year=2026), 'Complete the demo', datetime(day=25, month=1, year=2027))