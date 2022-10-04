# Bradley Grose

import game as g
import scoreboard as score
import pygame_menu
import pygame
import time


WIDTH = 800
HEIGHT = 800
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SIZE = 20
NAME = ""


quitTrigger = False

pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyGame Snake")
clock = pygame.time.Clock()


def gameLoop():

    currX = WIDTH / 2
    currY = HEIGHT / 2
    quitTrigger = False
    menuHold = False
    moveX = 0
    moveY = 0
    snakeList = []
    snakeLength = 1
    SPEED = g.getSpeed()
    score.resetScore()

    foodX, foodY = g.genFood(WIDTH, HEIGHT, SIZE)

    while not quitTrigger:

        while menuHold:
            g.menu(display, WIDTH, HEIGHT)
            show = score.addScore()
            if (show):
                showScore()
            time.sleep(5)
            menuStart(display, WIDTH, HEIGHT)
            gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitTrigger = True
            if event.type == pygame.KEYDOWN:
                moveX, moveY = g.movement(
                    moveX, moveY, SIZE, event.key, display, WIDTH, HEIGHT)

        if currX >= WIDTH-SIZE or currX < SIZE or currY >= HEIGHT-SIZE or currY < SIZE:
            menuHold = True

        currX += moveX
        currY += moveY

        display.fill(BLACK)

        # draw border around screen
        pygame.draw.rect(display, WHITE, (0, 0, WIDTH, HEIGHT), SIZE)

        pygame.draw.rect(display, GREEN, [currX, currY, SIZE, SIZE])
        pygame.draw.rect(display, RED, [foodX, foodY, SIZE, SIZE])
        print(SPEED)

        # put score top left
        TopMesg = pygame.font.SysFont("comicsansms", 15)
        display.blit(TopMesg.render(score.scoreMessage(), True, RED), (0, 0))
        display.blit(TopMesg.render(
            "Press Space to pause", True, RED), (WIDTH-150, 0))

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

        if (currX == foodX and currY == foodY):
            score.update()
            foodX, foodY = g.genFood(WIDTH, HEIGHT, SIZE)
            snakeLength += 1

        clock.tick(SPEED)


def set_difficulty(value, difficulty):
    if difficulty == 1:
        g.setSpeed(20)
        print("EASY")
    elif difficulty == 2:
        g.setSpeed(40)
        print("HARD")


def showScore():
    display.fill(BLACK)
    mesg = pygame.font.SysFont("timesnewroman", 30)
    listPrint = score.printScoreBoard()
    adjust = 0
    for i in listPrint:
        display.blit(mesg.render(i, True, WHITE), (WIDTH/2-100, 50+adjust))
        adjust += 30

    print(score.printScoreBoard())
    pygame.display.update()
    time.sleep(5)
    menuStart(display, WIDTH, HEIGHT)


def menuStart(display, WIDTH, HEIGHT):
    menu = pygame_menu.Menu('Welcome', WIDTH, HEIGHT,
                            theme=pygame_menu.themes.THEME_BLUE)

    menu.add.selector(
        'Difficulty :', [('EASY', 1), ('HARD', 2)], onchange=set_difficulty)

    menu.add.button('Play', gameLoop)
    menu.add.button('High Scores', showScore)
    menu.add.button('Quit', pygame_menu.events.EXIT)

    menu.mainloop(display)

    if menu.is_enabled() == False:
        gameLoop()


menuStart(display, WIDTH, HEIGHT)
