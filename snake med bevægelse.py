import pygame
import random 
import math 

#score
score = 0
high_score = 0 
pygame.init()

WIDTH = 600
HEIGHT = 600
title = "Snake game"

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption(title)
font = pygame.font.Font("freesansbold.ttf", 20)
big_font = pygame.font.Font("freesansbold.ttf", 50)
timer = pygame.time.Clock()
fps = 7

tile_size = 40
snake=[(4,7),(3,7),(2,7)]
direction = (1,0)


def death():
    screen.fill("black")
    gameOverTekst = big_font.render("Game Over", True, "green", "blue")
    screen.blit(gameOverTekst, (WIDTH/2 -120, HEIGHT/2 -80))
    
    restartTekst = big_font.render("Restart", True, "white")

    button = pygame.Rect(180, 300, 280, 50)
    restart_rect = pygame.draw.rect(screen, "red", button)
    screen.blit(restartTekst, (180, 300))

    if button.collidepoint(mousePos) and event.type == pygame.MOUSEBUTTONDOWN:
        print("skibidi button works")

    









run = True 
alive = True

while run:
    timer.tick(fps)
    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        mousePos = pygame.mouse.get_pos()
        #print(mousePos)

        if event.type == pygame.KEYDOWN and alive:
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and direction != (0,1):
                direction = (0,-1)
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and direction != (0,-1):
                direction = (0,1)
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and direction != (1,0):   
                direction = (-1,0)
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and direction != (-1,0):
                direction = (1,0)




    # BEVÆG SLANGEN
    if alive:
        head_x, head_y = snake[0]
        new_head = (head_x + direction[0], head_y + direction[1])

    
        # TEGN GRID
    for x in range(0, WIDTH, tile_size):
        pygame.draw.line(screen, "dark green", (x,0),(x,HEIGHT))
    for y in range(0, HEIGHT, tile_size):
        pygame.draw.line(screen, "dark green", (0,y),(WIDTH,y))

    
 

    # TJEK BORDER
    if new_head[0] < 0 or new_head[0] >= WIDTH // tile_size or \
       new_head[1] < 0 or new_head[1] >= HEIGHT // tile_size:
        alive = False
        death()
    else:
        snake.insert(0, new_head)
        snake.pop()

 
    # TEGN SLANGEN
    for x, y in snake:
        pygame.draw.rect(screen, "lime", (x*tile_size, y*tile_size, tile_size, tile_size), border_radius=12)

    pygame.display.flip()

pygame.quit()
