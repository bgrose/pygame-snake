"""Imports"""
import datetime

"""Constants"""
RED = (255, 0, 0)

"""Data Variables"""
scoreboard = []
global score
score = 0

"""
:summary: Updates the score by 1
"""


def update():
    global score
    score += 1


"""
:summary: Returns the score
:return: The score
"""


def getScore():
    return score


"""
:summary: Construct Score Message
:return: The score message
"""


def scoreMessage():

    ScoreString = "Score: " + str(getScore())
    return ScoreString


"""
:summary: Put togehter the score board
:return: The score board list 
"""


def highScoreBoard():
    sortScoreBoard()
    return printScoreBoard()


"""
:summary: resets score
"""


def resetScore():
    global score
    score = 0


"""
:summary: Check if score is worth of scoreboard
:return: True if score is worth of scoreboard to show
"""


def addScore():
    sortScoreBoard()
    if len(scoreboard) < 5:
        scoreboard.append({"date": datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M"), "score": getScore()})
        print(scoreboard)
        sortScoreBoard()
        return True
    else:
        if (getScore() > scoreboard[4]["score"]):
            scoreboard[4] = ({"date": datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M"), "score": getScore()})
            sortScoreBoard()
            print(scoreboard)
            return True

    sortScoreBoard()
    return False


"""
:summary: Lambda function to sort the scoreboard
"""


def sortScoreBoard():
    # Sort scoreboard by score
    scoreboard.sort(key=lambda x: x["score"], reverse=True)


"""
:summary: Creates the List to Hold Scoreboard String
:return: The Scoreboard String List
"""


def printScoreBoard():
    ret = []
    # Make scoreboard string
    ret.append("High Scores:")
    for i in range(0, len(scoreboard)):
        ret.append(str(i+1) + ":  " +
                   str(scoreboard[i]["score"]) + "  " + str(scoreboard[i]["date"]))
    return ret
