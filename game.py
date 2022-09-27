import pygame
import time


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