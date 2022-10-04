"""Imports"""
import datetime
import json
import os

"""Constants"""
RED = (255, 0, 0)

"""Data Variables"""
scoreboard = []
global score
score = 0
name = ""

"""
:summary: Updates the score by 1
"""


def update():
    global score
    score += 1
    
    
def setName(_name):
    global name
    name = _name

def getName():
    return name

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


def addScore(speed):

    if (speed == 20):
        difficulty = "Easy"
    elif (speed == 40):
        difficulty = "Hard"
    sortScoreBoard()
    if len(scoreboard) < 5:
        scoreboard.append({"date": datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M"), "score": getScore(), "difficulty": difficulty, "name": getName()})
        print(scoreboard)
        sortScoreBoard()
        writeScoreBoard()
        return True
    else:
        if (getScore() > scoreboard[4]["score"]):
            scoreboard[4] = ({"date": datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M"), "score": getScore(), "difficulty": difficulty, "name": getName()})
            sortScoreBoard()
            print(scoreboard)
            writeScoreBoard()
            return True

    writeScoreBoard()
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
                   str(scoreboard[i]["name"]) + "  " + str(scoreboard[i]["score"]) + "  " + str(scoreboard[i]["date"] + "  " + str(scoreboard[i]["difficulty"])))
    return ret


"""
:summary: Reads Scoreboard from JSON
"""


def readScoreBoard():
    global scoreboard
    # check if file exists
    if (os.path.isfile("scoreboard.json")):
        with open("scoreboard.json", "r") as f:

            if (os.stat("scoreboard.json").st_size != 0):
                scoreboard = json.load(f)
            else:
                scoreboard = []
    else:
        scoreboard = []


"""
:summary: Writes Scoreboard to JSON
"""


def writeScoreBoard():
    if (os.path.isfile("scoreboard.json")):
        jsonFile = open("scoreboard.json", "w")
        jsonFile.write(json.dumps(scoreboard, indent=2))
        jsonFile.close()
