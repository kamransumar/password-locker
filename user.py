from user_accounts import UserAccounts


class User:
    def __init__(self, first_name, last_name, email, password, platforms):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.platforms = platforms

    def save_user(self):
        user_list = [
            self.first_name,
            self.last_name,
            self.email,
            self.password,
            self.platforms,
        ]
        return user_list

    def add_account(self, account):
        self.platforms.append(account)


def main():
    print("Hello there, sign up here\n")
    first_name = input("enter first name \n")
    second_name = input("enter second name here\n")
    email = input("enter a valid email\n")
    password = input("create you password\n")

    new_user = User(first_name, second_name, email, password, []).save_user()

    if first_name != "" and second_name != "" and email != "" and password != "":

        print(f"Alright {new_user[0]} here are your account details")


if __name__ == "__main__":
    main()

