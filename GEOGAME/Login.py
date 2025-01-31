import sqlite3, time

# making a function to login
# verifying login details
def login():
    for i in range(3):
        username = input("Enter your username:")
        password = input("Enter your password:")
        with sqlite3.connect("Quiz.db") as db:
            cursor = db.cursor()
            find_user = ('SELECT * FROM user WHERE username = ? AND password = ?')
            cursor.execute(find_user, [(username), (password)])  # [] replaces the values of the ?
            results = cursor.fetchall()

        if results:
            for i in results:
                print("Welcome " + i[2])

                return (i[0])

        else:
            print("Username and password not recognised")
            again = input("Do you want to retry?(Y/N)")
            if again.lower() == "n":
                print("Goodbye")
                time.sleep(1)
                return ("exit")
