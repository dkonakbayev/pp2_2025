import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

# Основные параметры
fps = 60
width, height = 400, 600
speed = 5
score, point = 0, 0
N = 5  # Увеличение скорости за каждые N очков

# Цвета и шрифты
red = (255, 0, 0)
black = (0, 0, 0)
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, black)

# Фон и экран
background = pygame.image.load("C:/Users/Daulet/Desktop/pp2/lab8/raser/street.webp")
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Racer")
t = pygame.time.Clock()

# Вражеская машина
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("c:/Users/Daulet/Desktop/pp2/lab8/raser/Enemy.webp")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)

    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if self.rect.bottom > height + 80:
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, width - 40), 0)

# Монета
class Money(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("C:/Users/Daulet/Desktop/pp2/lab8/raser/money.png")
        self.rect = self.image.get_rect()
        self.respawn()

    def move(self):
        self.rect.move_ip(0, speed)
        if self.rect.bottom > height + 80:
            self.respawn()

    def respawn(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40, width - 40), 0)
        self.value = random.randint(1, 3)  # Разные очки за монету

# Машина игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("C:/Users/Daulet/Desktop/pp2/lab8/raser/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (width/2, height - 80)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top > 0 and pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if self.rect.bottom < height and pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < width and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

# Создание объектов
P1 = Player()
E1 = Enemy()
M1 = Money()

# Группы спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)

cash = pygame.sprite.Group()
cash.add(M1)

all_sprites = pygame.sprite.Group()
all_sprites.add(M1, P1, E1)

# Событие увеличения скорости
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            speed += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))

    # Отображение очков
    screen.blit(font_small.render(f"Score: {score}", True, black), (10, 10))
    screen.blit(font_small.render(f"Coins: {point}", True, black), (300, 10))


    # Движение и отрисовка спрайтов
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    # Проверка столкновения игрока с врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        screen.fill(red)
        screen.blit(game_over, (30, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Проверка сбора монет
    collected = pygame.sprite.spritecollide(P1, cash, False)
    for coin in collected:
        point += coin.value  # Начисляем очки
        coin.respawn()
        if point % N == 0:
            speed += 0.5 # Увеличение скорости

    pygame.display.update()
    t.tick(fps)
