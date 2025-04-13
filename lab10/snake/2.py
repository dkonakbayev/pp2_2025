import pygame
import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(dbname="phonebook", user="postgres", password="12345", host="localhost")
cur = conn.cursor()

# Инициализация pygame
pygame.init()

# Размеры окна
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

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

        if not paused:
            # Здесь будет обновление игры: например, увеличение счёта и уровня
            score += 1
            if score % 10 == 0:  # Каждые 10 очков увеличиваем уровень
                level += 1

        # Обновление экрана
        screen.fill((0, 0, 0))  # Чёрный фон
        pygame.display.update()

    pygame.quit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    start_game()
