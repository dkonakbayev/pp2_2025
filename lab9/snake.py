import pygame
import time
import random

pygame.init()

# Цвета и размер экрана
white = (255, 255, 255)
black = (0, 0, 0)
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
snake_block = 10
font = pygame.font.SysFont("Verdana", 20)

# Функции для отображения уровня и очков
def your_level(level):
    screen.blit(font.render("Level: " + str(level), True, white), (700, 10))

def your_point(point):
    screen.blit(font.render("Points: " + str(point), True, white), (10, 10))

# Функция для отрисовки змейки
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, white, [x[0], x[1], snake_block, snake_block])

# Генерация еды с разным весом и временем исчезновения
def generate_food():
    return {
        "x": round(random.randrange(0, width - snake_block) / 10.0) * 10.0,
        "y": round(random.randrange(0, height - snake_block) / 10.0) * 10.0,
        "value": random.randint(1, 3),  # Случайное количество очков (1–3)
        "spawn_time": time.time()  # Время появления еды
    }

def gameLoop():
    game_over = False
    x1, y1 = width / 2, height / 2
    x1_change, y1_change = 0, 0
    snake_List = []
    Length_of_snake = 1
    snake_speed = 15
    level, point = 0, 0

    food = generate_food()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change, y1_change = -snake_block, 0
                elif event.key == pygame.K_RIGHT:
                    x1_change, y1_change = snake_block, 0
                elif event.key == pygame.K_UP:
                    x1_change, y1_change = 0, -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change, y1_change = 0, snake_block

        # Если змейка вышла за границы — конец игры
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_over = True

        screen.fill(black)
        your_level(level)
        your_point(point)

        x1 += x1_change
        y1 += y1_change

        # Отображение еды
        pygame.draw.rect(screen, white, [food["x"], food["y"], snake_block, snake_block])

        # Обновление позиции змейки
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Проверка на столкновение с собой
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_over = True

        our_snake(snake_block, snake_List)
        pygame.display.update()

        # Проверка, съела ли змейка еду
        if x1 == food["x"] and y1 == food["y"]:
            Length_of_snake += 1
            point += food["value"]  # Начисление очков за еду
            food = generate_food()  # Генерация новой еды

            if point % 5 == 0:
                level += 1
                snake_speed += 5  # Увеличение скорости

        # Удаление еды через 5 секунд после появления
        if time.time() - food["spawn_time"] > 10:
            food = generate_food()

        clock.tick(snake_speed)

    pygame.quit()

gameLoop()
