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
big_font = pygame.font.Font("freesansbold.ttf", 25)
timer = pygame.time.Clock()
fps = 7

tile_size = 40
snake=[(4,7),(3,7),(2,7)]
direction = (1,0)

run = True 
alive = True



# RANDOM FRUITGENERATION
def CREATETHEREDDOTFORHELVEDE():
    while True:
        FruitPos = (random.randrange(0, WIDTH // tile_size), 
                random.randrange(0,HEIGHT // tile_size))
        
        # NO FRUIT INSIDE SNAKE BODY
        if FruitPos not in snake:
            return FruitPos

fruit = CREATETHEREDDOTFORHELVEDE()

while run:
    timer.tick(fps)
    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN and alive:
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and direction != (0,1):
                direction = (0,-1)
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and direction != (0,-1):
                direction = (0,1)
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and direction != (1,0):   
                direction = (-1,0)
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and direction != (-1,0):
                direction = (1,0)

    # MOVE SNAKE
    if alive:
        head_x, head_y = snake[0]
        new_head = (head_x + direction[0], head_y + direction[1])

    # CHECK BORDER
    if new_head[0] < 0 or new_head[0] >= WIDTH // tile_size or \
       new_head[1] < 0 or new_head[1] >= HEIGHT // tile_size:
        alive = False
    else:
        snake.insert(0, new_head)
        snake.pop()
    # DRAW GRID
    for x in range(0, WIDTH, tile_size):
        pygame.draw.line(screen, "dark green", (x,0),(x,HEIGHT))
    for y in range(0, HEIGHT, tile_size):
        pygame.draw.line(screen, "dark green", (0,y),(WIDTH,y))

    # DRAW SNAKE
    for x, y in snake:
        pygame.draw.rect(screen, "lime", (x*tile_size, y*tile_size, tile_size, tile_size), border_radius=12)

    # GENERATE FRUIT
    pygame.draw.rect(
        screen, "red",
        (fruit[0]*tile_size, fruit[1]*tile_size, tile_size, tile_size), border_radius=12)

    # GROWS SNAKE
    if new_head == tuple(fruit):
        #print("fruit eaten")
        
        snake.insert(0,new_head)
        fruit = CREATETHEREDDOTFORHELVEDE()
    
    # DIE IF SNAKE EATS ITSELF
    if new_head == (snake):
        alive = False

    pygame.display.flip()

pygame.quit()
