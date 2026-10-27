from __future__ import annotations

from .Employee import Employee
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Team import Team


class Team_Leader(Employee):
    """A team leader owns one or more teams and can assign tasks to team members and review their progress."""

    def __init__(self, id, fname, lname, email):
        super().__init__(id, fname, lname, email, tasks=[])
        

    def assign_task(self, task, team: Team, team_member: Employee) -> bool:
        if team_member in team.get_members():
            print(f"Task '{task}' assigned to {team_member.get_full_name()}.")
            return True
        else:
            print(f"Error: {team_member.get_full_name()} is not a member of the team.")
            return False

    def review_progress(self, team: Team):
        print(f"Reviewing progress for team members: {[member.get_full_name() for member in team.get_members()]}\n")

lead1 = Team_Leader(id=1111, fname='John', lname='Smith', email='john.smith@make-it-all.co.uk')
