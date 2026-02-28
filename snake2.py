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

tile_size = 40
snake=[(4,7),(3,7),(2,7)] # startpostition for hoved kroppen og hlen 
direction = (tile_size,0) 

run = True 

while run:
    timer.tick(fps)
    screen.fill("black")

    # event input handling
    # hvis spilleeren går ud af vinduet så slut spillet
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    for x in range (0, WIDTH, tile_size):
        pygame.draw.line(screen, "dark green", (x,0),(x,HEIGHT))
    for y in range (0,HEIGHT, tile_size):
        pygame.draw.line(screen, "dark green", (0,y),(WIDTH,y))
    for x, y in snake:
        pygame.draw.rect(screen, "lime", (x*tile_size, y*tile_size, tile_size, tile_size),border_radius=12)
    
    pygame.display.flip()  # Opdater skærmen

pygame.quit()  # Skal være uden for løkken




