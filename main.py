# Bradley Grose

import game as g
import pygame
import random



# Constants
WIDTH = 800
HEIGHT = 800
GREEN = (0,255,0)
RED = (255,0,0)
SIZE = 20

quitTrigger = False

#Set up the display
pygame.init()
display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("PyGame Snake")
clock = pygame.time.Clock()

# Holder Variables


def gameLoop():
    currX = WIDTH / 2
    currY = HEIGHT / 2
    Score = 0
    quitTrigger = False
    menuHold = False
    moveX = 0
    moveY = 0
    snakeList = []
    snakeList.append([currX, currY])
    
    foodX, foodY = g.genFood(WIDTH, HEIGHT, SIZE)
    
    while not quitTrigger:
        
        while menuHold:
            quitTrigger = g.menu(display, WIDTH, HEIGHT)
            gameLoop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitTrigger = True
            if event.type == pygame.KEYDOWN:
                moveX, moveY = g.movement(moveX, moveY, SIZE, event.key)
                    
        if currX >= WIDTH or currX < 0 or currY >= HEIGHT or currY < 0:
            menuHold = True
        
        currX += moveX
        currY += moveY
        
    
        display.fill((0,0,0))
        pygame.draw.rect(display, GREEN, [currX, currY, SIZE, SIZE])
        pygame.draw.rect(display, RED, [foodX,foodY,SIZE,SIZE])
        Scoremesg = pygame.font.SysFont("comicsansms", 20)
        ScoreString = "Score: " + str(Score)
        # put score top left
        display.blit(Scoremesg.render(ScoreString, True, (255,255,255)), (0,0))
        
        
        pygame.display.update()
        
        if(currX == foodX and currY == foodY):
            Score += 1
            foodX, foodY = g.genFood(WIDTH, HEIGHT, SIZE)
            snakeList = g.growSnake(snakeList, SIZE)
        clock.tick(15)


gameLoop()