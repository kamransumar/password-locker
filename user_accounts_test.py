import unittest

from user_accounts import UserAccounts

"""class that tests the user accounts"""


class TestUserAccounts(unittest.TestCase):
    def setUp(self):
        self.new_accounts = UserAccounts("facebook", "kamransumar@gmail.com", "God786")

    def test_init(self):
        self.assertEqual(self.new_accounts.name, "facebook")
        self.assertEqual(self.new_accounts.email, "kamransumar@gmail.com")
        self.assertEqual(self.new_accounts.password, "God786")

    def test_save_user_accounts(self):
        print(len(self.new_accounts.save_user_accounts()))
        self.assertEqual(len(self.new_accounts.save_user_accounts()), 3)
        print("ok")

    def test_gen_details(self):
        print(self.new_accounts.gen_details(8))


if __name__ == "__main__":
    unittest.main()
