import pygame
import random 
import math 

pygame.init()


print(pygame.version.ver)

WIDTH = 600
HEIGHT = 600
title = "Snake game"

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption(title)
font = pygame.font.Font("freesansbold.ttf", 20)
big_font = pygame.font.Font("freesansbold.ttf", 25)
timer = pygame.time.Clock()
fps = 60


run = True 

while run:
    timer.tick(fps)
    screen.fill("dark green")

    # event input handling
    # hvis spilleeren går ud af vinduet så slut spillet
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    
    pygame.display.flip()  # Opdater skærmen

pygame.quit()  # Skal være uden for løkken











