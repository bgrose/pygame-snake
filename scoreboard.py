import datetime
RED = (255, 0, 0)
scoreboard = []

global score
score = 0


def update():
    global score
    score += 1


def getScore():
    return score


def scoreMessage():

    ScoreString = "Score: " + str(getScore())
    return ScoreString


def getScore():
    return score


def highScoreBoard():
    sortScoreBoard()
    return printScoreBoard()


def resetScore():
    global score
    score = 0


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


def sortScoreBoard():
    # Sort scoreboard by score
    scoreboard.sort(key=lambda x: x["score"], reverse=True)


def printScoreBoard():
    ret = []
    # Make scoreboard string
    ret.append("High Scores:")
    for i in range(0, len(scoreboard)):
        ret.append(str(i+1) + ":  " +
                   str(scoreboard[i]["score"]) + "  " + str(scoreboard[i]["date"]))
    return ret
