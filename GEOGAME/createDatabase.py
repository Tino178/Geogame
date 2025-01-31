import sqlite3, time #imports the sqlite3 library which adds functionality to the program

#creates a connection with the quiz database 
with sqlite3.connect("Quiz.db") as db:
    cursor = db.cursor() #cursor will execute sql queries

#creating the user table - where all user details will be stored
#creates table with userID as primary key
#VARCHAR is a variable length string data type, it holds characters user assigns to it
cursor.execute('''
CREATE TABLE IF NOT EXISTS user(
userID INTEGER PRIMARY KEY, 
username VARCHAR(20) NOT NULL, 
firstname VARCHAR(20) NOT NULL, 
surname VARCHAR(20) NOT NULL,
password VARCHAR(20) NOT NULL);
''')

#creates a record to test if working
cursor.execute("""
INSERT INTO user (username,firstname,surname,password)
VALUES("test_User","Bob","Smith","MrBob")
""")
db.commit() #saves the record

cursor.execute("SELECT * FROM user")
print(cursor.fetchall())


#creation of topics table
#creates table with topicID as primary key 
cursor.execute('''
CREATE TABLE IF NOT EXISTS topics(
topicID INTEGER PRIMARY KEY,
topicName VARCHAR(20) NOT NULL);''')

#creation of scores table
#userID links scores table to the user table
#topicID links scores table to topic table
cursor.execute('''
CREATE TABLE IF NOT EXISTS scores(
scoreID INTEGER PRIMARY KEY,
userID INTEGER NOT NULL ,
score INTEGER NOT NULL,
topicID INTEGER NOT NULL,
FOREIGN KEY(userID) REFERENCES user(userID),
FOREIGN KEY(topicID) REFERENCES topics(topicID));''')

#questions table
#questionID is used as primary key in this table
#topicID links questions table to topic table
cursor.execute('''
CREATE TABLE IF NOT EXISTS questions(
questionID INTEGER PRIMARY KEY,
topicID INTEGER NOT NULL,
question VARCHAR(50),
option1 VARCHAR(50),
option2 VARCHAR(50),
option3 VARCHAR(50),
option4 VARCHAR(50),
answer VARCHAR(50),
FOREIGN KEY(topicID) REFERENCES topics(topicID));''')

#a query that selects all the tables that have been created
tables = cursor.execute('''
SELECT name FROM sqlite_master
WHERE type='table'
ORDER BY name;''')
print(cursor.fetchall())
