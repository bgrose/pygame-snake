# Bradley Grose

import game as g
import pygame



# Constants
WIDTH = 800
HEIGHT = 800
GREEN = (0,255,0)
SIZE = 20

quitTrigger = False

#Set up the display
pygame.init()
display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("PyGame Snake")
clock = pygame.time.Clock()

# Holder Variables
currX = WIDTH / 2
currY = HEIGHT / 2
quitTrigger = False
moveX = 0
moveY = 0


# Game Loop
while not quitTrigger:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitTrigger = True
        if event.type == pygame.KEYDOWN:
            moveX, moveY = g.movement(moveX, moveY, SIZE, event.key)
                
    if currX >= WIDTH or currX < 0 or currY >= HEIGHT or currY < 0:
        quitTrigger = True
    
    # Move the snake new position
    currX += moveX
    currY += moveY
    display.fill((0,0,0))
    pygame.draw.rect(display, GREEN, [currX,currY,SIZE,SIZE])
    
    pygame.display.update()
    clock.tick(30)

# Game Over
g.gameOver(display, WIDTH, HEIGHT)