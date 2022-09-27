import pygame
import time
import random


def gameOver(display, WIDTH, HEIGHT):
    display.fill((0,0,0))
    # Print Game Over
    mesg = pygame.font.SysFont("comicsansms", 72)
    display.blit(mesg.render("Game Over", True, (255,255,255)), (WIDTH/2 -150, HEIGHT/2))
    
    pygame.display.update()
    time.sleep(5)
    pygame.quit()
    quit()
    return 0
    
def movement(moveX, moveY, SIZE, key):
    if key == pygame.K_LEFT:
        moveX = -SIZE
        moveY = 0
    elif key == pygame.K_RIGHT:
        moveX = SIZE
        moveY = 0
    elif key == pygame.K_UP:
        moveX = 0
        moveY = -SIZE
    elif key == pygame.K_DOWN:
        moveX = 0
        moveY = SIZE
    return moveX, moveY

def menu(display, WIDTH, HEIGHT):
    display.fill((0,0,0))
    # Print Game Over
    mesg = pygame.font.SysFont("comicsansms", 25)
    display.blit(mesg.render("You Lost, click space to replay or esc to quit", True, (255,255,255)), (WIDTH/2 -150, HEIGHT/2))
    pygame.display.update()
    
    wait = True
    
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return False
                elif event.key == pygame.K_ESCAPE:
                    gameOver(display, WIDTH, HEIGHT)
                    return True #redundent
                
def genFood(WIDTH, HEIGHT, SIZE):
    foodX = round(random.randrange(0, WIDTH - SIZE) / 20.0) * 20.0
    foodY = round(random.randrange(0, HEIGHT - SIZE) / 20.0) * 20.0
    return foodX, foodY

def growSnake(snakeList, SIZE):
    snakeHead = []
    snakeHead.append(snakeList[-1][0])
    snakeHead.append(snakeList[-1][1])
    snakeList.append(snakeHead)
    return snakeList