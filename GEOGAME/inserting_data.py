import sqlite3 #importing the sqlite3 library to add functionality
#inserting_data

with sqlite3.connect("Quiz.db") as db: #connects to the quiz database
    cursor = db.cursor()

#the topics the user can select for a quiz
cursor.execute("""INSERT OR IGNORE INTO topics (topicName)
                   VALUES
                   ("Europe"),
                   ("Asia"),
                   ("Africa"),
                   ("All continents")""")

db.commit() #this commits all changes to the database

#inserts questions and multiple choice options into the questions table
#topic id corresponds to the topic selected by the user
cursor.execute("""INSERT OR IGNORE INTO questions
                   (topicID, question,
                   option1, option2, option3, option4, answer) 
                   VALUES
                   ("1", "What is the capital city of France?",
                    "Paris", "Minsk", "Athens", "Rome", "1"),
                   ("1", "What is the capital city of Germany?",
                    "Vienna", "Budapest", "Berlin", "Monaco", "3"),
                   ("1", "What is the capital city of Norway?",
                    "Warsaw", "Oslo", "Lisbon", "Bern", "2"),
                   ("1", "What is the capital city of Sweden?",
                    "Stockholm", "Belgrade", "Kiev", "Vienna", "1")
                """)
db.commit() #this commits all changes to the database

#adds more questions to each quiz topic 
cursor.execute("""INSERT OR IGNORE INTO questions
                   (topicID, question,
                   option1, option2, option3, option4, answer) 
                   VALUES
                   ("2", "What is the capital city of China?",
                    "Baku", "Beijing", "Tehran", "Tokyo", "2"),
                    
                    ("2", "What is the capital city of Israel?",
                    "Amman", "Kabul", "Paris", "Jerusalem", "4"),
                    
                   ("3", "What is the capital city of Kenya?",
                    "Nairobi", "Dakar", "Tokyo", "Brussels", "1"),
                    
                   ("3", "What is the capital city of Zimbabwe?",
                    "Harare", "Dijbouti", "Kampala", "Cairo", "1"),
                    
                    ("3", "What is the capital city of Zambia?",
                    "Cape Town", "Freetown", "Lusaka", "Brazzaville", "3"),
                    
                    ("3", "What is the capital city of South Sudan?",
                    "Oslo", "Kiev", "Vienna", "Juba", "4"),
                    
                    ("4", "What is the capital city of Fiji?",
                    "Alofi", "Port Vila",
                        "Apia", "Suva", "4"),
                        
                   ("4", "What is the capital city of Australia?",
                        "Wellington", "Funafuti", "Canberra", "Melbourne", "3")
                """)

db.commit()
