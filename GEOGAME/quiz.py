import sqlite3, time

def quiz(userID, topicID):
    with sqlite3.connect("Quiz.db") as db:
        cursor = db.cursor()

    score = 0
    cursor.execute("SELECT * FROM questions WHERE topicID=?",[(topicID)])
    questions = cursor.fetchall()
    numOfQuestions = 0 #used to help work out the score/percentage
    
    #print("\Here we go, you selected..", topic) - not actually a line was testing something
    for question in questions:
        topic = question[1]
        print(question[2])
        print("1.%s \n 2.%s \n 3.%s \n 4.%s" % (question[3], question[4], question[5], question[6]))
        choice = input("Answer: ")
        if choice == question[7]:
            print("Correct")
            score += 1
            time.sleep(2)
            print("")
        else:
            print("Incorrect")
        numOfQuestions+=1
    # works out percentage to keep all quiz scores consistent despite number of questions in topic
    if score > 0:
        score = int((score/numOfQuestions)*100)
    print("Your score was:",score)
    #stores results of quiz in the scores table
    insertData=("INSERT INTO scores(userID,score,topicID) VALUES(?,?,?);")
    cursor.execute(insertData, [(userID), (score), (topic)])
    db.commit()
    


#def showScores(user):
#    with sqlite3.connect("Quiz.db") as db:
#        cursor = db.cursor()
#
#   query = ("""SELECT topics.topicName, scores.score, user.userID
#    FROM user INNER JOIN (topics INNER JOIN scores ON topics.topicID = scores.topicID) ON user.userID = scores.userID
#    WHERE (((user.userID)=?));""")
#    cursor.execute(query, [(user)])
#    results = cursor.fetchall()
#    for line in results:
#        print(line[0], str(line[1]) + "%")

def showScores(userID): # send in a userID that has some results
   
    with sqlite3.connect ("Quiz.db") as db:
        cursor = db.cursor()

        # convert user ID from integer to list
        # to allow injection into SQL
        userID = [userID]    # converts to list
        print(type(userID))  # test

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
        print(sql)
       
        cursor.execute(sql, userID) #the userID list
                                                    #goes in here
       
        results = cursor.fetchall()
        print(results)      #print out results list
        #more infomrative printout
        for line in results:
            print(line[0], line[1], line[2] , "%")

showScores(2)
