# Bradley Grose

"""Imports"""
import game as g
import scoreboard as score
import pygame_menu
import pygame
import time


"""Constants"""
WIDTH = 800
HEIGHT = 800
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SIZE = 20
NAME = ""

"""Game Loop Trigger"""
quitTrigger = False

"""Startup"""
pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyGame Snake")
clock = pygame.time.Clock()

"""
:summary Game Loop for the game
"""


def gameLoop():
    """Game Variables"""
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

    """ Run the game loop """
    while not quitTrigger:

        """ Game is over next step """
        while menuHold:
            g.menu(display, WIDTH, HEIGHT)
            show = score.addScore()
            if (show):
                showScore()
            time.sleep(5)
            menuStart(display, WIDTH, HEIGHT)
            gameLoop()

        """ Event Handling """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitTrigger = True
            if event.type == pygame.KEYDOWN:
                moveX, moveY = g.movement(
                    moveX, moveY, SIZE, event.key, display, WIDTH, HEIGHT)

        """ Game Logic of Walls """
        if currX >= WIDTH-SIZE or currX < SIZE or currY >= HEIGHT-SIZE or currY < SIZE:
            menuHold = True

        """ Game Logic of Movement """
        currX += moveX
        currY += moveY

        """ Display Update """
        display.fill(BLACK)
        pygame.draw.rect(display, WHITE, (0, 0, WIDTH, HEIGHT), SIZE)
        pygame.draw.rect(display, GREEN, [currX, currY, SIZE, SIZE])
        pygame.draw.rect(display, RED, [foodX, foodY, SIZE, SIZE])
        TopMesg = pygame.font.SysFont("comicsansms", 15)
        display.blit(TopMesg.render(score.scoreMessage(), True, RED), (0, 0))
        display.blit(TopMesg.render(
            "Press Space to pause", True, RED), (WIDTH-150, 0))

        """ Game Logic of SnakeBody """
        snakeHead = []
        snakeHead.append(currX)
        snakeHead.append(currY)
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLength:
            del snakeList[0]
        g.drawSnake(snakeList, SIZE, display)

        """ Game Logic of SnakeBody Collisions """
        for x in snakeList[:-1]:
            if x == snakeHead:
                menuHold = True

        """ Game Logic of Food """
        if (currX == foodX and currY == foodY):
            score.update()
            foodX, foodY = g.genFood(WIDTH, HEIGHT, SIZE)
            snakeLength += 1

        """ Update the display """
        clock.tick(SPEED)
        pygame.display.update()


"""
:summary: Sets the difficulty of the game
:param value: The value of the difficulty (not used)
:param difficulty: The difficulty of the game
"""


def set_difficulty(value, difficulty):
    if difficulty == 1:
        g.setSpeed(20)
        print("EASY")
    elif difficulty == 2:
        g.setSpeed(40)
        print("HARD")


"""
:summary: Shows the High Score Board
"""


def showScore():
    display.fill(BLACK)
    mesg = pygame.font.SysFont("timesnewroman", 30)
    listPrint = score.printScoreBoard()
    adjust = 0

    """ Print the Score Board (Weird Adjust for Pygame) """
    for i in listPrint:
        display.blit(mesg.render(i, True, WHITE), (WIDTH/2-100, 50+adjust))
        adjust += 30

    print(score.printScoreBoard())
    pygame.display.update()
    time.sleep(5)
    menuStart(display, WIDTH, HEIGHT)


"""
:summary: Menu Runner for the game
:param display: The display of the game
:param WIDTH: The width of the game
:param HEIGHT: The height of the game
"""


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


"""Start the game"""
menuStart(display, WIDTH, HEIGHT)
