import unittest
from user import User
from user_accounts import UserAccounts


class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("kamran", "sumar", "kamransumar@gmail.com", "God786", [])
        self.new_accounts = UserAccounts("facebook", "kamransumar@gmail.com", "God786")
        self.new_accounts2 = UserAccounts("insta", "gigihadid@gmail.com", "Holy786")

    def test_init(self):
        self.assertEqual(self.new_user.first_name, "kamran")
        self.assertEqual(self.new_user.last_name, "sumar")
        self.assertEqual(self.new_user.email, "kamransumar@gmail.com")
        self.assertEqual(self.new_user.password, "God786")
        self.assertEqual(self.new_user.platforms, [])

    def test_save_user(self):
        print(len(self.new_user.save_user()))
        self.assertEqual(len(self.new_user.save_user()), 5)

    def test_add_account(self):
        account = self.new_accounts.save_user_accounts()
        account2 = self.new_accounts2.gen_details(8)
        self.new_user.add_account(account)
        self.new_user.add_account(account2)
        print(self.new_user.platforms)


if __name__ == "__main__":
    unittest.main()

