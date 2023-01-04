
# Import a library of functions called 'pygame'
import pygame
import random

# Initialize the game engine
pygame.init()

ballx = 150
bally = 200
# Set the height and width of the screen
SIZE = [400, 400]
clock = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE)
ballxchange = 5
ballychange = 5
while True:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            running = False

    screen.fill((0,115,0))
    pygame.draw.rect(screen,(96,91,120),(0,300,400,300))
    pygame.draw.rect(screen,(0,0,0),(350,90,25,210))
    pygame.draw.circle(screen,(255,140,120),(ballx,bally),10)
    pygame.draw.rect(screen,(255,0,0),(350,300,400,300))
    pygame.draw.rect(screen,(255,0,0),(280,150,70,10))
    clock.tick(20)
    pygame.display.flip()
    ballx += ballxchange
    bally -= ballychange
    if bally < 110:
        ballychange *= -1
    if bally > 350:
        break
