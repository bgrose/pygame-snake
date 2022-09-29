# Bradley Grose

from turtle import update
import game as g
import scoreboard as score
import pygame
import random



# Constants
WIDTH = 800
HEIGHT = 800
GREEN = (0,255,0)
RED = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
SIZE = 20
SPEED = 15

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
    quitTrigger = False
    menuHold = False
    moveX = 0
    moveY = 0
    snakeList = []
    snakeLength = 1
    
    foodX, foodY = g.genFood(WIDTH, HEIGHT, SIZE)
    
    while not quitTrigger:
        
        while menuHold:
            quitTrigger = g.menu(display, WIDTH, HEIGHT)
            if quitTrigger == True:
                break
            gameLoop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitTrigger = True
            if event.type == pygame.KEYDOWN:
                moveX, moveY = g.movement(moveX, moveY, SIZE, event.key, display, WIDTH, HEIGHT)
                    
        if currX >= WIDTH-SIZE or currX < SIZE or currY >= HEIGHT-SIZE or currY < SIZE:
            menuHold = True
        
        currX += moveX
        currY += moveY
        
    
        display.fill(BLACK)
        
        #draw border around screen
        pygame.draw.rect(display, WHITE, (0,0,WIDTH,HEIGHT), SIZE)
        
        pygame.draw.rect(display, GREEN, [currX, currY, SIZE, SIZE])
        pygame.draw.rect(display, RED, [foodX,foodY,SIZE,SIZE])

        # put score top left
        TopMesg = pygame.font.SysFont("comicsansms", 15)
        display.blit(TopMesg.render(score.scoreMessage(), True, RED), (0,0))
        display.blit(TopMesg.render("Press Space to pause", True, RED), (WIDTH-150,0))
        
        
        snakeHead = []
        snakeHead.append(currX)
        snakeHead.append(currY)
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLength:
            del snakeList[0]
        
        for x in snakeList[:-1]:
            if x == snakeHead:
                menuHold = True
                
        g.drawSnake(snakeList, SIZE, display)
        
        
        pygame.display.update()
        
        if(currX == foodX and currY == foodY):
            score.update()
            foodX, foodY = g.genFood(WIDTH, HEIGHT, SIZE)
            snakeLength += 1
        clock.tick(SPEED)
        



gameLoop()