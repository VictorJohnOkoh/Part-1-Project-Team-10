from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.productivity_app.users.Project import Project

class Employee:
    def __init__(self, id: int, first_name: str, last_name: str, email: str, tasks: list[Project]|None = None):
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__tasks = tasks if tasks is not None else []

    def get_id(self) -> int:
        return self.__id

    def get_email(self) -> str:
        return self.__email

    def get_full_name(self) -> str:
        return f"{self.__first_name} {self.__last_name}"

    def get_first_name(self) -> str:
        return self.__first_name

    def get_last_name(self) -> str:
        return self.__last_name

    def get_tasks(self) -> list[Project]:
        return self.__tasks

    def add_task(self, task) -> None:
        self.__tasks.append(task)

    def remove_task(self, task) -> None:
        self.__tasks.remove(task)

    def __str__(self) -> str:
        return f"Employee ID: {self.__id}, Name: {self.__first_name} {self.__last_name}, Email: {self.__email}, Tasks: {[task.get_name() for task in self.__tasks]}"