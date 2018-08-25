class User ( ):

    def __init__(self, first_name, last_name, email, password, platforms):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.platforms = platforms

    def save_user(self):
        user_list = [self.first_name, self.last_name, self.email, self.password, self.platforms]
        return user_list
