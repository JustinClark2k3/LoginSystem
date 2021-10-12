import tkinter_base as tkBase

class Login(tkBase.TkinterBase):
    def on_return_pressed(self, event):
        username = self.stringvar_1.get()
        password = self.stringvar_2.get()

        if username not in self.info.credentials.keys():
            print("Invalid Username")
            return

        if password not in self.info.credentials.values():
            print("Invalid password")
            return

        print("You're in!")

    def create_account(self, event):
        uname = self.stringvar_1.get()
        password = self.stringvar_2.get()

        if uname not in self.info.credentials.keys() and password not in self.info.credentials.values():
            self.info.credentials[uname] = password

            print("Credentials: ")
            print(self.info.credentials)
        else:
            print("Account already exists")