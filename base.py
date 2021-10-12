'''
This is a docstring
'''
import tkinter as tk

class Info:
    credentials = { "TestUsername" : "TestPassword" } 

'''
Login class that talks to the tkinter api and adds widgets, binds keys, and styles widgets
'''
class Login:

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

    def __init__(self, master):
        self.master = master

        self.info = Info()

        # Pre-Widget Window Modificatins
        master.title("login here!")
        master.geometry("600x400")

        # Frame to house widgets
        self.mainframe = tk.Frame(master)

        # Username and Password label widgets inside the frame
        self.label_01 = tk.Label(self.mainframe, text="Username")
        self.label_02 = tk.Label(self.mainframe, text="Password")

        self.button_submit = tk.Button(self.mainframe, text="Submit")
        self.button_create = tk.Button(self.mainframe, text="Create Account")

        # StringVar types for Entries
        self.stringvar_1 = tk.StringVar()
        self.stringvar_2 = tk.StringVar()

        self.text_01 = tk.Entry(self.mainframe, textvariable=self.stringvar_1)
        self.text_02 = tk.Entry(self.mainframe, textvariable=self.stringvar_2)

        # Set StringVars for Entries
        self.stringvar_1.set("Username")
        self.stringvar_2.set("Password")

        self.label_01.pack(expand=True)
        self.text_01.pack(expand=True)

        self.label_02.pack(expand=True)
        self.text_02.pack(expand=True)

        self.button_submit.pack(expand=True)
        self.button_create.pack(expand=True)

        self.mainframe.pack(padx=200, pady=100)

        self.master.bind(
            '<Return>', lambda event: self.on_return_pressed(self))
        
        self.button_create.bind(
            '<Button>', lambda event: self.create_account(self))
            
        self.button_submit.bind(
            '<Button>', lambda event: self.on_return_pressed((self)))

root = tk.Tk()
login = Login(root)
root.mainloop()
