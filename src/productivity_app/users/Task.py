import datetime

# Tasks are assigned to employees on a team, that team owns a project which the task belongs to. Each task has a name, description, and deadline.

class Task:
    def __init__(self, name: str, description: str, deadline: datetime.datetime):
        self.__name = name
        self.__description = description
        self.__deadline = deadline

    def get_name(self) -> str:
        return self.__name

    def get_description(self) -> str:
        return self.__description

    def get_deadline(self) -> datetime.datetime:
        return self.__deadline