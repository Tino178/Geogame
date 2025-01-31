import tkinter as tk #imports tkinter and allows me to refer to it as tk for short
from tkinter import * #gets everything
import tkinter.messagebox as tkMessageBox
from tkinter.messagebox import showerror, showwarning, showinfo
import tkinter as ttk
from tkinter import messagebox as mb
import sqlite3
from itertools import chain
import time
from tkinter import IntVar
import matplotlib.pyplot as plt
import numpy as np

global score #global variable so that the score is accessible in all modules
global correct_answer #global variable for the correct answer of each question stored in db
global opt1
global opt2
global opt3
global opt4


score = 0 #varuable used to keep track of the user's score
counter = 10 #index of the second question for the next question label 
correct_answer = 7 #index of the answer (for the first question) in the database to be compared to the user answer
#will be incremented each time by +8 for the next question

opt1 = 11 #index of multiple choice of next question
opt2 = 12
opt3 = 13
opt4 = 14




#increment by 8 for next question
#user_answer value is not changing - remaining as 0

 
def showScores(userID): #sends in user_id as a parameter to get all their results
    global all_user_results
  
  
    
    with sqlite3.connect ("Quiz.db") as db: #connection to the database
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
       
        all_user_results = cursor.fetchall()
        print(all_user_results)      #print out results list
        #more infomrative printout
        homeWindow = tk.Tk() #windwow creation for scores table
        homeWindow.title("GeoGame") 
        homeWindow.config(bg = "#ffcc66")
        homeWindow.geometry("470x350")

        frameting = tk.Frame(homeWindow) #creating the frame where results will be dispplayed
        frameting.config(bg ="#ffcc66")#background colour of frame
        frameting.grid(column = 1, row = 0, padx = 10, pady = 10)
        frameting.place(x= 150, y = 45) #positioning the frame in the correct place using coordinates 

        screen_title = tk.Label(homeWindow, text = "Scores Table") #title for the screen
        screen_title.config(bg = "#ffcc66", font = ("Calibri bold", 20))
        screen_title.grid(column = 2, row = 0, pady = 5, sticky = "w")
        screen_title.place(x= 175, y = 10)
        

        i = 1 #grid places for each result to be stored
        
        heading = tk.Label(frameting, text = "Topic") #Topic header
        heading.config(bg = "#ffcc66", font = ("Calibri bold", 20))
        heading.grid(column = 0, row = 0, pady = 5, sticky = "w")
        
        percent_header = tk.Label(frameting, text = "Percentage") #Percentage header 
        percent_header.config(bg = "#ffcc66", font = ("Calibri bold", 20))
        percent_header.grid(column = 1, row = 0, pady = 5, sticky = "w")
        
        for line in all_user_results: #for each quiz taken by user
             
          print(line[0], line[1], line[2] , "%")#testing to see if it displays correct results
          display_topic = tk.Label(frameting, text = (line[1])) #display the topic 
          display_topic.config(bg = "#ffcc66", font = ("Calibri bold", 20))
          display_topic.grid(column = 0, row =i , pady = 5, sticky = "w")

          display_percent = tk.Label(frameting, text = (line[2] , "%")) #display the percentage acheived 
          display_percent.config(bg = "#ffcc66", font = ("Calibri bold", 20))
          display_percent.grid(column = 1, row =i , pady = 5, sticky = "w")
          i+=1 #incrementing grid postion (row) for next result
          
          





def graph_scores(userID):
    with sqlite3.connect("Quiz.db") as db: #connection to the Quiz database
        cursor = db.cursor()

## making sure the two empty lists will store values for the X and Y axis
    
        y = [] #empty list - no scores inserted yet
        xaxis = [] #empty list - no topics inserted yet

        userID = [userID] #converts to list
        

#userID = [userID]    # converts to list
#print(type(userID))  # used to test

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
        plt.title("Progress %") #the title of the graph screen


        plt.bar(x, y) #creates bar graph with axis
        plt.show() #displays bar graph of results
#graph(3)


def check_value():
  print(user_answer.get()) #checking to see if the variable of the radiobutton is working 

def check_ans(question_l, answer_1, answer_2, answer_3, answer_4): #check's user answer is correct or incorrect
  global counter #global variable so that it can be accessed in other modules
  global score #user's score
  global correct_answer #global variable for the correct answer found in db
  
  print(user_answer.get()) #checking user's answer
  print(int(q_details[correct_answer])) #checking the correct answer from db
  if user_answer.get() == int(q_details[correct_answer]): #checking if user's answer and db answer match
    print("correct") #checking 
    score = score + 1 #if correct, score increments by 1
    #makes a message box which says correct
    tk.messagebox.showinfo("Result: ", "Correct! Keep up the fantastic work!") #displays feeback to the user
    
  else:
    print("incorrect")#checking
    tk.messagebox.showinfo("Result: ", "Incorrect, don't worry keep trying")#displays feeback to the user 
  correct_answer += 8 #increments to answer for next question
  next_ques(question_l, answer_1, answer_2, answer_3, answer_4) #passing each label for the next question

    
     
#testing
def next_ques(question_l, answer_1, answer_2, answer_3, answer_4):
  global q_num #global variable so it is accessible in other modules
  global q_details #global variable so it is accessible in other modules
  global counter #index for question label
  global opt1 #index for answer1 label
  global opt2 #index for answer2 label
  global opt3 #index for answer3 label 
  global opt4 #index for answer4 label 
  global score #user's score
  
  if counter <= 74: #index number of the last question 
    question_l.config(text = q_details[counter]) #incrementing to the next question
    answer_1.config(text = q_details[opt1]) #incrementing to the next option
    answer_2.config(text = q_details[opt2])
    answer_3.config(text = q_details[opt3])
    answer_4.config(text = q_details[opt4])
    counter = counter + 8 #adding 8 to get the details of the next question 
    opt1 += 8 #increments the label for the answer1 of the next question
    opt2 += 8 #increments the label for the answer1 of the next question
    opt3 += 8 #increments the label for the answer1 of the next question
    opt4 += 8 #increments the label for the answer1 of the next question
    q_num +=1 #adds one to the question number after each one is answered/completed
    print("Question:",q_num) #used to track which question on
    print(counter) #used to test whether counter is incrementing as intended
  else:
    print("Quiz completed") #indicates that the quiz has ended
    total = str(score)+" out of "+str(q_num) #calcuates the number of correct questions
    tk.messagebox.showinfo("Score: ","Your score is "+total) #displays total score to the user
    with sqlite3.connect("Quiz.db") as db: #connecting to the database 
      cursor = db.cursor() #defining cursor 
      insertData=("INSERT INTO scores(userID,score,topicID) VALUES(?,?,?);") #inserting data into table
      cursor.execute(insertData, [(userID), (score), (topic)]) #sending values to the database
      db.commit() #commit changes to the database
      userMenu(user, menu) #returning back to the user menu screen 
  
              
    
  

#needs a parameter for topic ID
      
#q_details = list(chain.from_iterable(data))#creates a new list with records which makes it easier to access individual fields
#print(q_details)

#module for the quiz to work 
def quiz_screen(topic_selection):
  global user_answer #global the user answer so that it is accessible in other modules
  global q_details #questions record
  global data #questions list
  global q_num #quesrion number


  q_num = 0 #used to track the question number
  

 
  #select all question IDs for the same topic
  with sqlite3.connect("Quiz.db") as db: #connecting to database
    cursor = db.cursor()
    #selecting all questions in the same topic quiz 
    sql = '''SELECT * FROM questions WHERE topicID = ?;'''
    cursor.execute(sql, [topic_selection])
    data = cursor.fetchall()
    print(data)
    q_details = list(chain.from_iterable(data))#creates a new list with records which makes it easier to access individual fields
    print(q_details)
    



  
  #for question in q_details:
  #if answered == True: #variable to allow the user to answer a question one at a time
  #creating the background for the screen
  homeWindow = tk.Tk()
  homeWindow.title("GeoGame")
  homeWindow.config(bg = "#9DF1E9")
  homeWindow.geometry("470x350")
  user_answer = tk.IntVar()#declaring data type of user_answer 
  user_answer.set(0)#set initial value to 0
  print(user_answer)#check user_answer inital value
  q_num += 1
  print("Question:", q_num) #for checking purposes - which question user is on

  
  #label for each question that the user needs to answer
  question_l = tk.Label(homeWindow, text = q_details[2]) #displays text in question label 
  question_l.config(bg = "white", fg = "black", font = ("Arial Rounded MT Bold", 15), \
                                  width = 30, height = 2)
  question_l.grid(column = 1, row = 2, columnspan = 2, pady = 5)
  question_l.place(x = 70, y =35) #coordinates to place the question label 

  #creating the first answer button the user can select
  ans1 = tk.Radiobutton(homeWindow, \
                               value = 1, variable = user_answer) #assigning vlaue to each radiobutton and variable assignment so answer can checked against db answer
  ans1.config(bg = "#9DF1E9") #bg colour of the radiobutton is the same as homeWindow bg colour 
  ans1.grid(column = 1, row = 3, columnspan = 1, pady = 15)
  ans1.place(x =280, y=100 )
  #creating the label that will display the first option for the user
  answer_1 = tk.Label(homeWindow, text = q_details[3])
  answer_1.config(bg = "white", fg = "black", font = ("Calibri bold", 20), \
                                width = 15, height = 1)
  answer_1.grid(column = 1, row = 3, pady = 20, columnspan = 1)
  answer_1.place(x=10, y=95)

  #creating the second answer button the user can select
  ans2 = tk.Radiobutton(homeWindow, \
                               value = 2, variable = user_answer)#assigning a value to each button
  ans2.config(bg = "#9DF1E9")
  ans2.grid(column = 1, row = 3, columnspan = 1, pady = 15)
  ans2.place(x =280, y=150 )
  #creating the label that will display the second option for the user
  answer_2 = tk.Label(homeWindow, text = q_details[4])
  answer_2.config(bg = "white", fg = "black", font = ("Calibri bold", 20), \
                                width = 15, height = 1)
  answer_2.grid(column = 1, row = 3, pady = 20, columnspan = 1)
  answer_2.place(x=10, y=145)

  #creating the third answer button the user can select
  ans3 = tk.Radiobutton(homeWindow, \
                               value = 3, variable = user_answer)#assigning a value to each button
  ans3.config(bg = "#9DF1E9")
  ans3.grid(column = 1, row = 3, columnspan = 1, pady = 15)
  ans3.place(x =280, y=200 )
  #creating the label that will display the third option for the user
  answer_3 = tk.Label(homeWindow, text = q_details[5])
  answer_3.config(bg = "white", fg = "black", font = ("Calibri bold", 20), \
                                width = 15, height = 1)
  answer_3.grid(column = 1, row = 3, pady = 20, columnspan = 1)
  answer_3.place(x=10, y=195)  

  #creating the fourth answer button the user can select
  ans4 = tk.Radiobutton(homeWindow, \
                               value = 4, variable = user_answer) #assigning a value to each button
  ans4.config(bg = "#9DF1E9")
  ans4.grid(column = 1, row = 3, columnspan = 1, pady = 15)
  ans4.place(x =280, y=250 )
  #creating the label that will display the fourth option for the user
  answer_4 = tk.Label(homeWindow, text = q_details[6])
  answer_4.config(bg = "white", fg = "black", font = ("Calibri bold", 20), \
                                width = 15, height = 1)
  answer_4.grid(column = 1, row = 3, pady = 20, columnspan = 1)
  answer_4.place(x=10, y=245)


 

                
      #q_num = q_num + 1 #counts how many questions have been answered
      #if q_num == 10: #end of questions reached
        #pass#need to show the user's final score
           

  #creating the button for the user to submit their answer, it will run a function that verifies the answer selected
  submit_ans = tk.Button(homeWindow, text = "Submit", justify = "center", command = lambda: check_ans(question_l, answer_1, answer_2, answer_3, answer_4))
  submit_ans.config(bg = "white", fg = "black", font = ("Arial Rounded MT Bold", 15), \
                            width = 20, height = 2)
  submit_ans.grid(column = 1, row = 4, columnspan = 2, pady = 5)
  submit_ans.place(x =120, y=290)#places labels at specific coordinate







  
  

  
  
     
#user menu function where user can select quiz and view scores
def userMenu(user, name): #userID and username passed to module 
  global user_id #UserID of user that is logged in
  #creates screen
  background = "#ffaa80" #window background
  homeWindow = tk.Tk()
  homeWindow.title("GeoGame")
  homeWindow.config(bg = "#ffaa80")#User Menu Screen background colour 
  homeWindow.geometry("430x300")

  #displays a welcome message for the user 
  heading1 = tk.Label(homeWindow, text = "Welcome, "+name)
  heading1.config(bg = background, font = ("Arial Narrow", 18), \
                 width = 24, height = 1)
  heading1.grid(column = 0, row = 0, columnspan = 4)

  #button to go to quiz for European countries
  button1 = tk.Button(homeWindow, text = "Europe Quiz", command= lambda: quiz_screen(1) )
  button1.config(bg = "white", fg = "black", font = ("Calibri bold", 12), 
                width = 15, height = 1)
  button1.grid(column = 3, row = 1, columnspan = 1, pady = 5, sticky = "w" )

  #button to go to quiz for Asian countries
  button2 = tk.Button(homeWindow, text = "Asia Quiz", command= lambda: quiz_screen(2))
  button2.config(bg = "white", fg = "black", font = ("Calibri bold", 12), 
                width = 15, height = 1)
  button2.grid(column = 3, row = 2, columnspan = 1, pady = 5, sticky = "w" )

  #button to go to quiz for African countries
  button4 = tk.Button(homeWindow, text = "Africa Quiz", command= lambda: quiz_screen(3))
  button4.config(bg = "white", fg = "black", font = ("Calibri bold", 12), 
                width = 15, height = 1)
  button4.grid(column = 3, row = 3, columnspan = 1, pady = 5, sticky = "w" )

  #button to go to quiz for countries
  button5 = tk.Button(homeWindow, text = "All continents Quiz", command= lambda: quiz_screen(4))
  button5.config(bg = "white", fg = "black", font = ("Calibri bold", 12), 
                width = 15, height = 1)
  button5.grid(column = 3, row = 4, columnspan = 1, pady = 5, sticky = "w" )
  
  #button to view user scores
  button6 = tk.Button(homeWindow, text = "Show my scores", command = lambda: showScores(user_id))
  button6.config(bg = "white", fg = "black", font = ("Calibri bold", 12), 
                 width = 15, height = 1)
  button6.grid(column = 3, row = 5, columnspan = 1, pady = 5, sticky = "w" )
  
  #button to go to qgraph to display user scores
  button7 = tk.Button(homeWindow, text = "Graph", command= lambda: graph_scores(user_id))
  button7.config(bg = "white", fg = "black", font = ("Calibri bold", 12), 
                width = 15, height = 1)
  button7.grid(column = 3, row = 6, columnspan = 1, pady = 5, sticky = "w" )

  button8 = tk.Button(homeWindow, text = "Logout", command = main1)
  button8.config(bg = "white", fg = "black", font = ("Calibri bold", 12), 
                width = 15, height = 1)
  button8.grid(column = 4, row = 6, columnspan = 1, pady = 5, sticky = "w" )
    
  

  
  

#login screen where user can enter their details to access their account  
def login_page():
  #creates login screen
  background = "#CED8F6"
  homeWindow = tk.Tk()
  homeWindow.title("GeoGame")
  homeWindow.config(bg = "#CED8F6")
  homeWindow.geometry("430x300")

  #label displays heading of login screen to make the screen user-friendly
  heading1 = tk.Label(homeWindow, text = "Login")
  heading1.config(bg = background, font = ("Arial Narrow", 16), \
                 width = 19, height = 1)
  heading1.grid(column = 0, row = 0, columnspan = 4)

  #label to prompt the user to enter their username
  username1 = tk.Label(homeWindow, text= "Please enter your username")
  username1.config(bg = background, font = ("Calibri bold", 10))
  username1.grid(column = 1, row = 2, pady = 10, sticky = "w")
  #entry box for user to enter their username
  username1Enter = Entry(homeWindow)
  username1Enter.config(bg = "white", font = ("Calibri bold", 10))
  username1Enter.grid(column = 2, row = 2, columnspan = 2, pady =10)

  #label to prompt user to enter their password in entry box
  password1 = tk.Label(homeWindow, text="Please enter your password")
  password1.config(bg = background, font = ("Calibri bold", 10))
  password1.grid(column = 1, row = 3, pady = 10, sticky = "w")
  #entry box for user to enter their password
  password1Enter = Entry(homeWindow,show="*") #hides password field with asterisks for security purposes 
  password1Enter.config(bg = "white", font = ("Calibri bold", 10))
  password1Enter.grid(column = 2, row = 3, columnspan = 2, pady =10)


  def insertLoginData():#connected to the login screen
      global user_id #user_id from database if login details match 
      
      results = 0 #no record found yet
      username = str(username1Enter.get()) #get method for username entry
      password = str(password1Enter.get()) #get method for password entry
      print(username, password) #testing if entries have been recevied
      with sqlite3.connect("Quiz.db") as db: #connection to the Quiz database
          cursor = db.cursor()

         
          #validation - checks if the user's details are in the database
          find_user = ('SELECT * FROM user WHERE username = ? AND password = ?') #sql query to check if details are in the database
          cursor.execute(find_user, [(username), (password)])  # [] replaces the values of the ?
          results = cursor.fetchall()
          print(results) #displays record found
          #how to confirm to the user that their details have been found in the database
          if len(results) > 0: #validation - if record found
              print("Access granted") #user has gained access
              for i in results:
                  user = i[0] #userid
                  name = i[1] #username
                  user_id = results[0][0] #userID
                  print("User ID = ", user_id) #testing if user id matches one in the database
                  userMenu(user, name) #passes the userID and username to userMenu module
          else:
            #validation - message shown to user if login has failed
            mb.showinfo("Error", "Username or password not recognised")
            #validation - entry boxes are cleared, so user can re-enter details
            username1Enter.delete(0,'end')
            password1Enter.delete(0,'end')

  bottomFrame = Frame(homeWindow, width=200, height = 50) #frame for login and exit buttons
  bottomFrame.grid(row=7, column=1, padx = 10, pady = 2)

  #allows the user's details to be validated and checked against the database
  button1 = tk.Button(bottomFrame, text = "Login", command=insertLoginData) #button to verify login details
  button1.grid(row = 0, column = 1)
  button2 = tk.Button(bottomFrame, text = "Exit", command=main1, width = 10) #button to return back to homepage screen
  button2.grid(row = 0, column = 2)

  

  

  
def exit_program():
  pass


#create new user screen which allows user to create a new account
def create_user(homeWindow):
  background = "#CED8F6"
  homeWindow = tk.Tk()
  homeWindow.title("GeoGame")
  homeWindow.config(bg = "#CED8F6")
  homeWindow.geometry("470x350")

  #enter details
  heading1 = tk.Label(homeWindow, text = "Create New User")
  heading1.config(bg = background, font = ("Arial Narrow", 16), \
                 width = 19, height = 1)
  heading1.grid(column = 0, row = 0, columnspan = 4)

  #label to prompt the user to enter their firstname
  firstname = tk.Label(homeWindow, text="Please enter a first name")
  firstname.config(bg = background, font = ("Calibri bold", 10))
  firstname.grid(column = 1, row = 2, pady = 10, sticky = "w")
  firstnameEnter = Entry(homeWindow)
  firstnameEnter.config(bg = "white", font = ("Calibri bold", 10))
  firstnameEnter.grid(column = 2, row = 2, columnspan = 2, pady =10)

  #user's surname
  surname = tk.Label(homeWindow, text="Please enter your surname")
  surname.config(bg = background, font = ("Calibri bold", 10))
  surname.grid(column = 1, row = 3, pady = 10, sticky = "w")
  surnameEnter = Entry(homeWindow)
  surnameEnter.config(bg = "white", font = ("Calibri bold", 10))
  surnameEnter.grid(column = 2, row = 3, columnspan = 2, pady =10)
  
  #user's username
  username = tk.Label(homeWindow, text="Please enter your username")
  username.config(bg = background, font = ("Calibri bold", 10))
  username.grid(column = 1, row = 4, pady = 10, sticky = "w")
  usernameEnter = Entry(homeWindow)
  usernameEnter.config(bg = "white", font = ("Calibri bold", 10))
  usernameEnter.grid(column = 2, row = 4, columnspan = 2, pady =10)


  #user's password
  password = tk.Label(homeWindow, text="Please enter your password")
  password.config(bg = background, font = ("Calibri bold", 10))
  password.grid(column = 1, row = 5, pady = 10, sticky = "w")
  passwordEnter = Entry(homeWindow, show="*")
  passwordEnter.config(bg = "white", font = ("Calibri bold", 10))
  passwordEnter.grid(column = 2, row = 5, columnspan = 2, pady =10)

  #user is prompted to re-enter the password they entered
  password2 = tk.Label(homeWindow, text="Please enter your re-enter your password")
  password2.config(bg = background, font = ("Calibri bold", 10))
  password2.grid(column = 1, row = 6, pady = 10, sticky = "w")
  password2Enter = Entry(homeWindow, show="*")
  password2Enter.config(bg = "white", font = ("Calibri bold", 10))
  password2Enter.grid(column = 2, row = 6, columnspan = 2, pady =10)

  bottomFrame = Frame(homeWindow, width=200, height = 600)
  bottomFrame.grid(row=7, column=1, padx = 10, pady = 2)

  #details are sent to the database
  def insertNewData():
    #variable to check if username is already in the database
    found = 0
    firstName = str(firstnameEnter.get())
    new_surname = str(surnameEnter.get())
    f_password = str(passwordEnter.get())
    re_password = str(password2Enter.get())
    new_username = str(usernameEnter.get())
    #check databse to check if username is already taken
    with sqlite3.connect("Quiz.db") as db:
      cursor = db.cursor()

    sql = """SELECT * from user
          WHERE
          username = ?"""
    cursor.execute(sql, [new_username])
    results = cursor.fetchall()

    if results:
      #tells the user that the username has alreasy been taken
      print("the username is already taken") #print statement to check its working
      tk.messagebox.showinfo("Error", "Username is already taken")
      
    else:
      if f_password != re_password:  #if passwords do not match
        tk.messagebox.showinfo("Error: ", "Passwords do not match") #user show a message
        f_password.delete(0,'end')
        re_password.delete(0, 'end')
      else:
        #if validation checks are met, data is saved to the database
        insertData = '''INSERT INTO user(username,firstname, surname,password)
        VALUES(?,?,?,?)'''
        cursor.execute(insertData, [(new_username), (firstName), (new_surname), (f_password)])
        db.commit()
        tk.messagebox.showinfo("Result", "Success! ")#tells user record has been added successfully
        main1() #re-directs the user to the main screen
        
        
        
      
        
 


  #buttons to allow the user to submit their details 
  button1 = tk.Button(bottomFrame, text = "Submit", command=insertNewData)
  button1.grid(row = 0, column = 1)
  #Exit button to home page screen
  button2 = tk.Button(bottomFrame, text = "Exit", command=main1, width = 10)
  button2.grid(row = 0, column = 2)
  

  
  



  

  
  
  
  
  
  
  



###########setting the welcome window##########
def main1():
#def exit_program(): #module run for command on exit button 
#tk.messagebox.showinfo("Message: ", "Closing program...") #message to the user that the program is closing
#homeWindow.destroy() #window is closed
  homeWindow = tk.Tk()
  homeWindow.title("GeoGame")
  homeWindow.config(bg = "#8cd98c")
  homeWindow.geometry("470x350")

  frameting = tk.Frame(homeWindow)
  frameting.config(bg ="#8cd98c")
  frameting.grid(column = 0, row = 0, padx = 20, pady = 20)
  
  #heading on the screen
  heading1 = tk.Label(frameting, text = "Welcome to GeoGame")
  heading1.config(bg = "#80bfff", font = ("Calibri bold", 24), \
                 width = 19, height = 2)
  heading1.grid(column = 0, row = 0, columnspan = 4)

  #button to create an account
  button1 = tk.Button(frameting, text = "Create New\n User", command = lambda: create_user(homeWindow))
  button1.config(bg = "white", fg = "black", font = ("Calibri bold", 12), 
                width = 11, height = 2)
  button1.grid(column = 2, row = 1, columnspan = 1, pady = 10, sticky = "w" )
  
  #botton to login to user account
  button2 = tk.Button(frameting, text = "Login", command= login_page)
  button2.config(bg = "white", fg = "black", font = ("Calibri bold", 12), 
                width = 11, height = 2)
  button2.grid(column = 2, row = 2, columnspan = 1, pady = 10, sticky = "w" )
  
  #button to exit the program 
  button3 = tk.Button(frameting, text = "Exit", command= exit_program)
  button3.config(bg = "white", fg = "black", font = ("Calibri bold", 12), 
                width = 11, height = 2)
  button3.grid(column = 2, row = 3, columnspan = 1, pady = 10, sticky = "w" )

  
  homeWindow.mainloop()
#All the lines of code relating to the contents within the window must be placed before the mainloop function. In short, the mainloop is needed to make everything run/display.

main1()

