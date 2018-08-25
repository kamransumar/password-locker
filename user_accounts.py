class UserAccounts:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def save_user_accounts(self):
        user_account_list = [self.name, self.email, self.password]
        return user_account_list
