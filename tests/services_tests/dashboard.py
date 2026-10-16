import unittest
from src.productivity_app.users.Employee import Employee

class MyTestCase(unittest.TestCase):
    def test_access(self):
        user = Employee(1234, 'John', 'Smith', 'johnsmith@make-it-all.co.uk')
        self.assertFalse(, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
