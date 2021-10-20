class Login():
    def __init__(self):
        self.credentials = { "MyUsername": "MyPassword" }

    def on_return_pressed(self, event, action, p_username, p_password):
        if action == "create":
            self.create_account(p_username, p_password)
            return

        username = self.stringvar_1.get()
        password = self.stringvar_2.get()

        if username not in self.credentials.items():
            print("Invalid Credentials!")
            return

        # if username not in self.credentials.keys():
        #     print("Invalid Username")
        #     return

        # if password not in self.credentials.values():
        #     print("Invalid password")
        #     return

        # print("You're in!")

    def create_account(self, username, password):
        pass
        # uname = self.stringvar_1.get()
        # password = self.stringvar_2.get()

        # if uname not in self.credentials.keys():
        #     if password not in self.credentials.values():
        #         self.credentials[uname] = password

        #         print("Credentials: ")
        #         print(self.credentials)
        # else:
        #     print("Account already exists")
