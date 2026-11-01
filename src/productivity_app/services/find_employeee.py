from productivity_app.users.Employee import Employee

def get_employee(employees : list[Employee], email: str) -> Employee|None:
    for employee in employees:
        if employee.get_email() == email:
            return employee
        else:
            return None