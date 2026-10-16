class Task:
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description
