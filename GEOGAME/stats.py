import sqlite3, time
import matplotlib.pyplot as plt
import numpy as np
import quiz

def graph(userID):
    with sqlite3.connect("Quiz.db") as db:
        cursor = db.cursor()

## making sure the two empty lists will store values for the X and Y axis
    
        y = []
        xaxis = []

        userID = [userID]
        





#query = ("""SELECT topics.topicName, scores.score, user.userID
#FROM user INNER JOIN (topics INNER JOIN scores ON topics.topicID = scores.topicID) ON user.userID = scores.userID
#WHERE (((user.userID)=?));""")
#cursor.execute(query)
#results = cursor.fetchall()

#userID = [userID]    # converts to list
#print(type(userID))  # test

# this link statement should be used for any
# SELECT QUERIES using multiple tables
# just change the SELECT bit and the WHERE bit
       
        sql = '''SELECT user.userID, topics.topicName,
                                scores.score
                    FROM user INNER JOIN
                    (topics INNER JOIN scores
                    ON topics.topicID = scores.topicID)
                    ON user.userID = scores.userID
                    WHERE user.userID = ?;
                '''
#print(sql)
       
        cursor.execute(sql, userID) #the userID list
                                                    #goes in here
       
        results = cursor.fetchall()

## used to iterate through the results of the query to populate the lists
        for line in results:
            y.append(line[2])  # squiz score
            xaxis.append(line[1])  # topic name

## creates enough space for the names to be included on the x-axis in another list called "x"
        x = [i for i in range(len(y))]
        plt.xticks(x, xaxis)  # labels the x axis with the topic name

## telling the program to plot the axis from x and y
        plt.title("Progress %")


        plt.bar(x, y)
        plt.show()
#graph(3)
