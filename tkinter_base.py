'''
Base class to render the GUI with widgets and bind event handlers
'''
import tkinter as tk
import login

class TkinterBase:
    def get_input(self, action):
        username = self.stringvar_1.get()
        password = self.stringvar_2.get()

        self.login.on_return_pressed(self, action, username, password)

    def exit_program(self):
        print("Exiting Program...\n")
        self.master.destroy()

    def __init__(self, master):
        print("tkinter_base Initialized")

        self.master = master
        self.login = login.Login()

        self.credentials = { 
            "TestUsername" : "TestPassword" 
        }

        # Pre-Widget Window Modificatins
        master.title("Justin's Login")
        master.geometry("600x400")

        # Frame to house widgets
        self.mainframe = tk.Frame(master)

        # Username and Password label widgets inside the frame
        self.label_01 = tk.Label(self.mainframe,
            text="Username"
        )

        self.label_02 = tk.Label(self.mainframe,
            text="Password"
        )

        # Bottom buttons
        self.button_submit = tk.Button(self.mainframe, text="Submit")
        self.button_create = tk.Button(self.mainframe, text="Create Account")
        self.button_exit = tk.Button(
            self.mainframe, 
            text="Exit", 
            command= lambda: self.exit_program()
        )

        # StringVar types for Entries
        self.stringvar_1 = tk.StringVar()
        self.stringvar_2 = tk.StringVar()

        self.text_01 = tk.Entry(self.mainframe, 
            textvariable=self.stringvar_1
        )

        self.text_02 = tk.Entry(self.mainframe,
            textvariable=self.stringvar_2
        )

        # Set StringVars for Entries
        self.stringvar_1.set("Username")
        self.stringvar_2.set("Password")

        self.label_01.pack(expand=True)
        self.text_01.pack(expand=True)

        self.label_02.pack(expand=True)
        self.text_02.pack(expand=True)

        self.button_submit.pack(expand=True)
        self.button_create.pack(expand=True)
        self.button_exit.pack(expand=True)

        self.mainframe.pack(padx=200, pady=100)

        self.master.bind(
            '<Return>', lambda event: self.get_input("login")
        )

        self.button_submit.bind(
            '<Button>', lambda event: self.get_input("login")
        )

        self.button_create.bind(
            '<Button>', lambda event: self.get_input("create")
        )

root = tk.Tk()
TkinterBase(root)
root.mainloop()
