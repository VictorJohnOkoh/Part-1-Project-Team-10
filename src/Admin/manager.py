class Manager:

    def __init__(self, id: int, email: str, fname: str, lname: str):
        self.id = id
        self.email = email
        self.fname = fname
        self.lname = lname

    def get_name(self) -> str:
        """Returns the full name of the person"""
        return self.fname + ' ' + self.lname
        
    