import sqlite3
import time
import Login
import menus

#making a function to add a user
def newUser():
    print("Add a new user")
    time.sleep(1)
    # check is username is taken
    found = 0
    while found == 0:
        username = input("Enter a username: ")
        with sqlite3.connect("Quiz.db") as db:
            cursor = db.cursor()
        find_user = ('SELECT * FROM user WHERE username = ?')  # ? stops SQL injection
        cursor.execute(find_user,[(username)])  # [] replaces the values of the ?

        if cursor.fetchall():
            print("Username Taken")
            # will then allow the user to re-enter a username
            ask = input("Would you like to exit the program? (Y/N)")
            if ask.lower() == "y":
                return ("exit")

        else:
            found = 1

    if found == 1:
        firstName = input("Please enter your first name: ")
        surname = input("Please enter your last name: ")
        password = input("Please enter a password: ")
        password1 = input("Please re-enter a password: ")
        while password != password1:
            print("Passwords did not match")
            password = input("Please enter a password: ")
            password1 = input("Please re-enter a password: ")

        insertData = '''INSERT INTO user(username,firstname, surname,password)
        VALUES(?,?,?,?)'''
        cursor.execute(insertData, [(username), (firstName), (surname), (password)])
        db.commit()  # saves the results to the database


# making a menu to run the functions
while True:
    print("Welcome to the system")
    menu = ('''
    1 - Create New User
    2 - Login
    3 - Exit \n''')

    userChoice = input(menu)
    if userChoice == "1":
        newUser()

    elif userChoice == "2":
        user = Login.login()
        if user == "exit":
            break
        else:
            print("Starting quiz")
            time.sleep(1)
            menus.userMenu(user)


    elif userChoice == "3":
        print("Goodbye")
        time.sleep(1)
        break

    else:
        print("Input not recognised, please try again")
