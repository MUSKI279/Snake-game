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
big_font = pygame.font.Font("freesansbold.ttf", 28)
timer = pygame.time.Clock()

fps = 7
level = 0

tile_size = 40
snake = [(4, 7), (3, 7), (2, 7)]
direction = (1, 0)

def create_fruit():
    while True:
        fruit_pos = (random.randrange(0, WIDTH // tile_size),
                     random.randrange(0, HEIGHT // tile_size))
        if fruit_pos not in snake:
            return fruit_pos

fruit = create_fruit()

run = True
alive = True
start_screen = True
difficulty = None


def start_menu():
    screen.fill("black")

    title_text = big_font.render("Choose Difficulty", True, "green")
    title_rect = title_text.get_rect(center=(WIDTH // 2, 150))
    screen.blit(title_text, title_rect)

    # Buttons
    easy_btn = pygame.Rect(180, 250, 280, 50)
    normal_btn = pygame.Rect(180, 330, 280, 50)
    hard_btn = pygame.Rect(180, 410, 280, 50)

    pygame.draw.rect(screen, "green", easy_btn)
    pygame.draw.rect(screen, "yellow", normal_btn)
    pygame.draw.rect(screen, "red", hard_btn)

    screen.blit(font.render("Easy", True, "black"), (280, 265))
    screen.blit(font.render("Normal", True, "black"), (270, 345))
    screen.blit(font.render("Hard", True, "black"), (285, 425))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if easy_btn.collidepoint(mouse_pos):
                return "easy"
            if normal_btn.collidepoint(mouse_pos):
                return "normal"
            if hard_btn.collidepoint(mouse_pos):
                return "hard"

    return None


def death():
    screen.fill("black")
    game_over_text = big_font.render("Game Over", True, "red", "black")
    game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(game_over_text, game_over_rect)

    restart_text = font.render("Restart on:", True, "white")
    restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
    screen.blit(restart_text, restart_rect)

    easy_btn = pygame.Rect(100, 300, 120, 50)
    normal_btn = pygame.Rect(240, 300, 120, 50)
    hard_btn = pygame.Rect(380, 300, 120, 50)

    pygame.draw.rect(screen, "green", easy_btn)
    pygame.draw.rect(screen, "yellow", normal_btn)
    pygame.draw.rect(screen, "red", hard_btn)

    screen.blit(font.render("Easy", True, "black"), (easy_btn.x + 30, easy_btn.y + 15))
    screen.blit(font.render("Normal", True, "black"), (normal_btn.x + 15, normal_btn.y + 15))
    screen.blit(font.render("Hard", True, "black"), (hard_btn.x + 30, hard_btn.y + 15))

    score_text = font.render(f"Score: {score}  High Score: {high_score}", True, "white")
    score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 70))
    screen.blit(score_text, score_rect)

    level_text = font.render(f"Level: {level}", True, "white")
    screen.blit(level_text, (10, 40))

    return {"easy": easy_btn, "normal": normal_btn, "hard": hard_btn}


def reset_game():
    global snake, direction, fruit, alive, score, fps, level
    snake = [(4, 7), (3, 7), (2, 7)]
    direction = (1, 0)
    fruit = create_fruit()
    alive = True
    score = 0
    fps = 7
    level = 0


def update_fps():
    global fps, level, difficulty

    level = score // 4

    if difficulty == "easy":
        fps = 7
    elif difficulty == "normal":
        fps = 7 + (level * 3)
    elif difficulty == "hard":
        fps = 7 + (2 ** level)


def move_snake(snake, direction):
    head_x, head_y = snake[0]
    return (head_x + direction[0], head_y + direction[1])


def draw_grid():
    for x in range(0, WIDTH, tile_size):
        pygame.draw.line(screen, "dark green", (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, tile_size):
        pygame.draw.line(screen, "dark green", (0, y), (WIDTH, y))


def draw_snake(snake):
    for x, y in snake:
        pygame.draw.rect(
            screen, "lime",
            (x * tile_size, y * tile_size, tile_size, tile_size),
            border_radius=12)


def draw_fruit(fruit):
    pygame.draw.rect(
        screen, "red",
        (fruit[0] * tile_size, fruit[1] * tile_size, tile_size, tile_size),
        border_radius=12)


def draw_level(level):
    level_text = font.render(f"Level: {level}", True, "white")
    screen.blit(level_text, (10, 40))


game_over_buttons = {}

while run:
    timer.tick(fps)
    screen.fill("black")

    if start_screen:
        choice = start_menu()
        if choice:
            difficulty = choice
            start_screen = False
        pygame.display.flip()
        continue

    if not alive:
        game_over_buttons = death()
    else:
        game_over_buttons = {}

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

        if not alive and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for choice, button in game_over_buttons.items():
                if button.collidepoint(mouse_pos):
                    difficulty = choice
                    reset_game()
                    break

    if alive:
        new_head = move_snake(snake, direction)

        if new_head[0] < 0 or new_head[0] >= WIDTH // tile_size or \
           new_head[1] < 0 or new_head[1] >= HEIGHT // tile_size:
            alive = False
        elif new_head in snake:
            alive = False
        else:
            snake.insert(0, new_head)
            if new_head == fruit:
                score += 1
                if score > high_score:
                    high_score = score
                fruit = create_fruit()
                update_fps()
            else:
                snake.pop()

        draw_grid()
        draw_snake(snake)
        draw_fruit(fruit)
        draw_level(level)

        score_text = font.render(f"Score: {score}", True, "white")
        screen.blit(score_text, (10, 10))

        fps_text = font.render(f"FPS: {fps}", True, "white")
        screen.blit(fps_text, (10, 70))

    pygame.display.flip()

pygame.quit()
