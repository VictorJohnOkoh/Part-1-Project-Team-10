from .Employee import Employee
from .Team import Team

# a team leader owns one or more teams and can assign tasks to team members and review their progress. 
# a team leader is also an employee, so they inherit the properties of an employee.
# 

class Team_Leader(Employee):
    def __init__(self, id, fname, lname, email, teams: list[Team]):
        super().__init__(id, fname, lname, email, tasks=[])
        self.teams = teams

    def assign_task(self, task, team: Team, team_member: Employee) -> bool:
        if team_member in team.get_members():
            print(f"Task '{task}' assigned to {team_member.get_full_name()}.")
            return True
        else:
            print(f"Error: {team_member.get_full_name()} is not a member of the team.")
            return False

    def review_progress(self, team: Team):
        print(f"Reviewing progress for team members: {[member.get_full_name() for member in team.get_members()]}\n")