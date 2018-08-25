import random
import string


class UserAccounts:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def save_user_accounts(self):
        user_account_list = [self.name, self.email, self.password]
        return user_account_list

    def gen_details(self, number):
        password = "".join(
            random.choices(string.ascii_uppercase + string.digits, k=number)
        )

        user_account_list = [self.name, self.email, password]

        return user_account_list
