import unittest
from user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("kamran", "sumar", "kamransumar@gmail.com", "God786", [])

    def test_init(self):
        self.assertEqual(self.new_user.first_name, "kamran")
        self.assertEqual(self.new_user.last_name, "sumar")
        self.assertEqual(self.new_user.email, "kamransumar@gmail.com")
        self.assertEqual(self.new_user.password, "God786")
        self.assertEqual(self.new_user.platforms, [])

    def test_save_user(self):
        print(len(self.new_user.save_user()))
        self.assertEqual(len(self.new_user.save_user()), 5)


if __name__ == "__main__":
    unittest.main()

