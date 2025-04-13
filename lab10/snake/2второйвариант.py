import pygame
import psycopg2
import random

# Подключение к базе данных
conn = psycopg2.connect(dbname="phonebook", user="postgres", password="12345", host="localhost")
cur = conn.cursor()

# Инициализация pygame
pygame.init()

# Размеры окна
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Размеры блоков
block_size = 20

# Функция для получения или создания пользователя
def get_or_create_user():
    username = input("Введите ваше имя пользователя: ")
    cur.execute("SELECT user_id, username FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    if user:
        print(f"Добро пожаловать, {username}! Продолжаем с того места, где вы остановились.")
        return user[0]  # Возвращаем user_id
    else:
        print(f"Привет, {username}! Давайте создадим ваш профиль.")
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING user_id", (username,))
        conn.commit()
        return cur.fetchone()[0]  # Возвращаем новый user_id

# Функция для получения текущего уровня пользователя
def get_current_level(user_id):
    cur.execute("SELECT level, score FROM users_score WHERE user_id = %s ORDER BY date DESC LIMIT 1", (user_id,))
    result = cur.fetchone()
    if result:
        level, score = result
        print(f"Ваш последний уровень: {level}, Счёт: {score}")
    else:
        print("У вас нет предыдущего результата. Начинаем с нуля!")

# Функция для сохранения состояния игры в базе данных
def save_score(user_id, level, score):
    cur.execute("INSERT INTO users_score (user_id, level, score) VALUES (%s, %s, %s)", (user_id, level, score))
    conn.commit()
    print(f"Игра сохранена: Уровень {level}, Счёт {score}")

# Основной игровой цикл
def start_game():
    user_id = get_or_create_user()
    get_current_level(user_id)

    level = 1
    score = 0
    snake = [(width // 2, height // 2)]  # Начальная позиция змейки
    direction = (0, -block_size)  # Начальное направление (вверх)
    apple = (random.randint(0, (width - block_size) // block_size) * block_size,
             random.randint(0, (height - block_size) // block_size) * block_size)
    speed = 15  # Начальная скорость
    running = True
    paused = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Клавиша 'P' для паузы
                    paused = not paused
                    if paused:
                        print("Игра на паузе. Нажмите 'P' для продолжения.")
                        save_score(user_id, level, score)
                    else:
                        print("Игра продолжена.")
                elif event.key == pygame.K_q:  # Завершение игры при нажатии 'Q'
                    running = False
                elif event.key == pygame.K_LEFT and direction != (block_size, 0):
                    direction = (-block_size, 0)
                elif event.key == pygame.K_RIGHT and direction != (-block_size, 0):
                    direction = (block_size, 0)
                elif event.key == pygame.K_UP and direction != (0, block_size):
                    direction = (0, -block_size)
                elif event.key == pygame.K_DOWN and direction != (0, -block_size):
                    direction = (0, block_size)

        if not paused:
            # Обновление позиции змейки
            new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
            snake.insert(0, new_head)

            # Проверка на столкновение с границами
            if new_head[0] < 0 or new_head[0] >= width or new_head[1] < 0 or new_head[1] >= height:
                print("Вы проиграли! Столкновение с границей.")
                save_score(user_id, level, score)
                break

            # Проверка на столкновение с собой
            if new_head in snake[1:]:
                print("Вы проиграли! Столкновение с телом змейки.")
                save_score(user_id, level, score)
                break

            # Поедание яблока
            if new_head == apple:
                apple = (random.randint(0, (width - block_size) // block_size) * block_size,
                         random.randint(0, (height - block_size) // block_size) * block_size)
                score += 1
                if score % 10 == 0:
                    level += 1
                    speed += 2  # Увеличиваем скорость игры

            else:
                snake.pop()  # Удаление хвоста змейки, если яблоко не съедено

            # Отрисовка
            screen.fill(BLACK)
            for segment in snake:
                pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], block_size, block_size))
            pygame.draw.rect(screen, RED, pygame.Rect(apple[0], apple[1], block_size, block_size))

            pygame.display.update()

            # Устанавливаем частоту кадров в зависимости от скорости
            pygame.time.Clock().tick(speed)

    pygame.quit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    start_game()
