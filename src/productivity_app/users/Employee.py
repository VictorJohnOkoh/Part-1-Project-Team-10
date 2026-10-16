from src.productivity_app.users import Task, Project

class Employee:
    def __init__(self, id: int, first_name: str, last_name: str, email: str, project: type[Project] = None,tasks: list[type[Task]]|None = None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tasks = tasks if tasks is not None else []
        self.project = project

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_first_name(self) -> str:
        return self.first_name

    def get_last_name(self) -> str:
        return self.last_name

    def get_tasks(self) -> list[type[Task]]:
        return self.tasks

    def add_task(self, task) -> None:
        self.tasks.append(task)

    def get_current_project(self):
        return self.project