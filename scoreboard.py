import pygame
RED = (255,0,0)


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

