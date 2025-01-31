import quiz
import stats


#hard-wired method
#user menu


def userMenu(user):
    while True:
        print("Welcome to the system ")
        menus = ('''
            1 - Europe Quiz
            2 - Asia Quiz
            3 - Africa Quiz
            4 - All continents Quiz
            5 - Show my scores
            6 - Graph
            7 - Exit /n''')

        userChoice = input(menus)

        if userChoice == "1":
            quiz.quiz(user,1)

        elif userChoice == "2":
            quiz.quiz(user,2)

        elif userChoice == "3":
            quiz.quiz(user,3)

        elif userChoice == "4":
            quiz.quiz(user,4)

        elif userChoice == "5":
            quiz.showScores(user)

        elif userChoice == "6":
            stats.graph(user)

        elif userChoice == "7":
            break
