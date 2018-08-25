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
        return self.platforms.append(account)


def main():
    print("Hello there, sign up here\n")
    first_name = input("enter first name \n")
    second_name = input("enter second name here\n")
    email = input("enter a valid email\n")
    password = input("create you password\n")

    user = User(first_name, second_name, email, password, [])
    new_user = user.save_user()

    if first_name != "" and second_name != "" and email != "" and password != "":

        print(f"Alright {new_user[0]} here are your account details\n\n")
        print(
            f"your full name is:  {new_user[0]} {new_user[1]}\n Your email : {new_user[2]}\n Your password : {new_user[3]}"
        )
        print(
            "to continue choose the following according to your prefrence:\n\n ac: to add existing account\n nc: generate new account details\n"
        )

        choice = input().lower()

        if choice == "ac":
            name = input("Enter acount name: \n")
            email = input("Enter a valid email\n")
            password = input("Enter a valid password\n")

            acc = UserAccounts(name, email, password).save_user_accounts()

            user.add_account(acc)

            print(new_user)


if __name__ == "__main__":
    main()

