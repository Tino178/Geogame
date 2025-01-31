import tkinter as tk #imports tkinter and allows me to refer to it as tk for short
import sqlite3

from tkinter import * #gets everything
from tkinter import messagebox

#conn = sqlite3.connect("Quiz.db")
#c = conn.cursor()

#def submit_details():
#    user = usernameEnter.get()
#    passw = passwordEnter.get()

#    print(f"The name entered by you is {user} {passw}")
    
#setting up the window
background = "#CED8F6"
newUserWindow = Tk()
newUserWindow.configure(background=background)
newUserWindow.geometry("430x300")
newUserWindow.title("GeoGame")


def insertData():
    pass

Label(newUserWindow, text="Create New User", font=("Arial Narrow", 16), bg=background).grid(row=0, column=0, columnspan=4)

username = Label(text="Please enter a username", bg=background).grid(row=2, column=1, sticky=W, pady=10)
usernameEnter = Entry()
usernameEnter.grid(row=2, column=2, columnspan=2, pady=10)
firstName = Label(text="Please enter your first name", bg=background).grid(row=3, column=1, sticky=W, pady=10)
firstNameEnter = Entry()
firstNameEnter.grid(row=3, column=2, columnspan=2, pady=10)
surname = Label(text="Please enter your surname", bg=background).grid(row=4, column=1, sticky=W, pady=10)
surnameEnter = Entry()
surnameEnter.grid(row=4, column=2, columnspan=2, pady=10)
password = Label(text="Please enter your password", bg=background).grid(row=5, column=1, sticky=W, pady=10)
passwordEnter = Entry(show="*")
passwordEnter.grid(row=5, column=2, columnspan=2, pady=10)
password2 = Label(text="Please re-enter your password", bg=background).grid(row=6, column=1, sticky=W, pady=10)
password2Enter = Entry(show="*")
password2Enter.grid(row=6, column=2, columnspan=2, pady=10, padx=10)


bottomFrame = Frame(newUserWindow, width=200, height=600)
bottomFrame.grid(row=7, column=1, padx=10, pady=2)

#purpose of button is to be able to allow the user to activate when a nevent takes place (e.g.when the user presses a button, it prompts a function to run)
Button(bottomFrame, text="Submit", command=insertData, width = 10).grid(row=0, column=1)
Button(bottomFrame, text="Exit", command=lambda: close_user_window(newUserWindow), width=10).grid(row=0, column=2)
#lambda - allows you in this instance to pass a value into the function, without it your system will produce an error.

newUserWindow.mainloop()
#All the lines of code relating to the contents within the window must be placed before the mainloop function. In short, the mainloop is needed to make everything run/display.
