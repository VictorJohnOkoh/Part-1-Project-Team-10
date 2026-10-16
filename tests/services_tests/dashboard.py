import unittest
from src.productivity_app.services import check_user, check_password

class LoginTests(unittest.TestCase):
    def test_wrong_user_and_pass(self):
        username = "ADMIN"
        password = "ADMIN"
        self.assertFalse(check_user(username) and check_password(password), False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
