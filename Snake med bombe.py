import pygame
import random 

# Score
score = 0
high_score = 0
pygame.init()

WIDTH = 600
HEIGHT = 600
title = "Snake game"

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption(title)
font = pygame.font.Font("freesansbold.ttf", 20)
big_font = pygame.font.Font("freesansbold.ttf", 35)
timer = pygame.time.Clock()
fps = 7
numberOfBombs = 10

tile_size = 40
snake=[(4,7),(3,7),(2,7)]
direction = (1,0)

head_x, head_y = snake[0]
new_head = (head_x + direction[0], head_y + direction[1])


# RANDOM FRUIT GENERATION
def create_fruit():
    while True:
        fruit_pos = (random.randrange(0, WIDTH // tile_size),
                     random.randrange(0, HEIGHT // tile_size))

        # NO FRUIT INSIDE SNAKE BODY
        if fruit_pos not in snake:
            return fruit_pos


def create_bomb():
    while True:

        nonBombArea = [
            (x, y)
            for x in range(head_x - 3, head_x + 4)
            for y in range(head_y - 3, head_y + 4)
        ]

        allBomb_pos = []
        for i in range(numberOfBombs):

            bomb_pos = (random.randrange(0, WIDTH // tile_size),
                        random.randrange(0, HEIGHT // tile_size))
            
            if bomb_pos not in snake and bomb_pos != fruit and bomb_pos not in allBomb_pos and bomb_pos not in nonBombArea:
                allBomb_pos.append(bomb_pos)
        
        if len(allBomb_pos) == numberOfBombs:
            return allBomb_pos
        

run = True
alive = True
started = False


# skaber dødskærm

def death():

    screen.fill("black")
    game_over_text = big_font.render("Game Over", True, "crimson", "black")
    game_over_rect = game_over_text.get_rect(center=(WIDTH//2, HEIGHT //2 -80))
    screen.blit(game_over_text, game_over_rect)

    restart_text = font.render("Click to Restart", True, "white")
    button = pygame.Rect(180, 300, 280, 50)
    pygame.draw.rect(screen, "red", button)
    screen.blit(restart_text, (190, 310))

    score_text = font.render(f"Score: {score}  High Score: {high_score}", True, "white")
    screen.blit(score_text, (WIDTH // 2 - 100, HEIGHT // 2 + 70))

    return button

def reset_game():
    global snake, direction, fruit, alive, score, started, bomb
    snake = [(4, 7), (3, 7), (2, 7)]
    direction = (1, 0)
    fruit = create_fruit()
    bomb = create_bomb()
    alive = True
    score = 0
    started = True



while run:
    timer.tick(fps)
    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        

        if event.type == pygame.KEYDOWN and alive:
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and direction != (0, 1):
                direction = (0, -1)
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and direction != (0, -1):
                direction = (0, 1)
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and direction != (1, 0):
                direction = (-1, 0)
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and direction != (-1, 0):
                direction = (1, 0)


        mouse_pos = pygame.mouse.get_pos()
        if not alive and event.type == pygame.MOUSEBUTTONDOWN:

            button = death()
            if button.collidepoint(mouse_pos):
                reset_game()
        
        if started == False and event.type == pygame.MOUSEBUTTONDOWN:

            if startButton.collidepoint(mouse_pos):
                reset_game()


    if started == False:
        snakeText = big_font.render("Snake Game", True, "green", "black")
        snakeTextPosition = snakeText.get_rect(center=(WIDTH // 2 , HEIGHT // 2 - 80))
        screen.blit(snakeText, snakeTextPosition)

        start_text = font.render("Start game", True, "white")
        startButton = pygame.Rect(180, 300, 280, 50)
        pygame.draw.rect(screen, "dark green", startButton)
        
        game_start_rec = start_text.get_rect(center=(310, 320))
        screen.blit(start_text, game_start_rec)

    else:
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

            # CHECK SELF COLLISION
                if new_head in snake[1:]:
                    alive = False
                else:
                # DIE IF SNAKE HITS BOMB
                    if new_head in bomb:
                        alive = False
                
                    else:
                    # GROW SNAKE IF IT EATS FRUIT
                        if new_head == fruit:
                            score += 1
                            if score > high_score:
                                high_score = score
                            fruit = create_fruit()
                            bomb = create_bomb()

                   
                        else:
                            snake.pop()

            # GENERATE FRUIT
            pygame.draw.rect(
                screen, "red",
                (fruit[0] * tile_size, fruit[1] * tile_size, tile_size, tile_size), border_radius=12)
            
            # GENERATE BOMBs
            for i in range(numberOfBombs):
                pygame.draw.rect(
                    screen, "darkgrey",
                    (bomb[i][0] * tile_size, bomb[i][1] * tile_size, tile_size, tile_size), border_radius=12)

        # DRAW GRID
        for x in range(0, WIDTH, tile_size):
            pygame.draw.line(screen, "dark green", (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, tile_size):
            pygame.draw.line(screen, "dark green", (0, y), (WIDTH, y))

        # DRAW SNAKE
        for x, y in snake:
            pygame.draw.rect(screen, "lime", (x * tile_size, y * tile_size, tile_size, tile_size), border_radius=12)

        # DRAW SCORE
        score_text = font.render(f"Score: {score}", True, "white")
        screen.blit(score_text, (10, 10))

        if not alive:
            death()
    
    pygame.display.flip()   

pygame.quit()
