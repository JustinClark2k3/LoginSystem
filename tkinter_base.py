'''
This is a docstring
'''
import tkinter as tk

class Info:
    credentials = { "TestUsername" : "TestPassword" } 

'''
Login class that talks to the tkinter api and adds widgets, binds keys, and styles widgets
'''
class TkinterBase:
    def __init__(self, master):
        print("tkinter_base Initialized")

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
        self.button_exit = tk.Button(self.mainframe, text="Exit", command=lambda event: self.master.destroy())

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

        #self.master.bind(
        #    '<Return>', lambda event: self.on_return_pressed(self))
        
        #self.button_create.bind(
        #    '<Button>', lambda event: self.create_account(self))
            
        #self.button_submit.bind(
        #    '<Button>', lambda event: self.on_return_pressed((self)))

root = tk.Tk()
TkinterBase(root)
root.mainloop()
