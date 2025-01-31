import sqlite3,time

with sqlite3.connect("Quiz.db") as db:
    cursor = db.cursor()
#planning the relational database


#topics table
cursor.execute('''
CREATE TABLE IF NOT EXISTS topics(
topicID INTEGER PRIMARY KEY,
topicName VARCHAR(20) NOT NULL);''')

#scores table
cursor.execute('''
CREATE TABLE IF NOT EXISTS scores(
scoreID INTEGER PRIMARY KEY,
userID INTEGER NOT NULL ,
score INTEGER NOT NULL,
topicID INTEGER NOT NULL,
FOREIGN KEY(userID) REFERENCES users(userID),
FOREIGN KEY(topicID) REFERENCES topics(topicID));''')

#questions table
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

tables = cursor.execute('''
SELECT name FROM sqlite_master
WHERE type='table'
ORDER BY name;''')
print(cursor.fetchall())
