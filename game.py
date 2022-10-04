"""Imports"""
import pygame
import time
import random
import scoreboard as score

"""Constants"""
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
SPEED = 20


"""   
:summary: Handles game over display (not used)
:param display: The display to draw on
:param WIDTH: The width of the display
:param HEIGHT: The height of the display 
"""


def gameOver(display, WIDTH, HEIGHT):
    display.fill((0, 0, 0))
    # Print Game Over
    mesg = pygame.font.SysFont("comicsansms", 72)
    display.blit(mesg.render("Game Over", True, WHITE),
                 (WIDTH/2 - 150, HEIGHT/2))

    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    quit()


"""
:summary: Movement Handler for the game
:param moveX: The x movement of the snake
:param moveY: The y movement of the snake
:param SIZE: The size of the snake
:param key: The key pressed
:param display: The display to draw on
:param WIDTH: The width of the display
:param HEIGHT: The height of the display
:return: The new moveX and moveY
"""


def movement(moveX, moveY, SIZE, key, display, WIDTH, HEIGHT):
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
    elif key == pygame.K_SPACE:
        pause(display, WIDTH, HEIGHT)

    return moveX, moveY


"""
:summary: Shows You Lost Screen
:param display: The display to draw on
:param WIDTH: The width of the display
:param HEIGHT: The height of the display
"""


def menu(display, WIDTH, HEIGHT):
    display.fill((0, 0, 0))
    # Print Game Over
    mesg = pygame.font.SysFont("comicsansms", 25)
    display.blit(mesg.render("You Lost! Score: " +
                 str(score.getScore()), True, WHITE), (WIDTH/2 - 150, HEIGHT/2))
    pygame.display.update()


"""
:summary: Generates Radnom Food
:param WIDTH: The width of the display
:param HEIGHT: The height of the display
:param SIZE: The size of the snake
:return: The x and y coordinates of the food
"""


def genFood(WIDTH, HEIGHT, SIZE):
    rerun = True
    foodX = round(random.randrange(SIZE, WIDTH - SIZE*2) / 20.0) * 20.0
    foodY = round(random.randrange(SIZE, HEIGHT - SIZE*2) / 20.0) * 20.0

    return foodX, foodY


"""
:summary: Draws the snake on the display
:param snakeList: The list of the snake cords
:param SIZE: The size of the snake
:param display: The display to draw on
"""


def drawSnake(snakeList, SIZE, display):
    for x in snakeList:
        pygame.draw.rect(display, GREEN, [x[0], x[1], SIZE, SIZE])


"""
:summary: Pause Screen
:param display: The display to draw on
:param WIDTH: The width of the display
:param HEIGHT: The height of the display
"""


def pause(display, WIDTH, HEIGHT):
    hold = True
    while (hold):
        mesg = pygame.font.SysFont("comicsansms", 25)
        display.blit(mesg.render("Click Space to resume",
                     True, WHITE), (WIDTH/2 - 150, HEIGHT/2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    hold = False


"""
:summary: Sets Speed of Snake
:param speed: The speed of the snake
"""


def setSpeed(speed):
    global SPEED
    SPEED = speed


"""
:summary: Gets speed of snake
:return: The speed of the snake
"""


def getSpeed():
    return SPEED
