import pygame
import math
import time
from datetime import datetime

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")


clock_face = pygame.image.load("C:/Users/Daulet/Downloads/clock.png")
clock_face = pygame.transform.scale(clock_face, (WIDTH, HEIGHT))  

# hands
right_hand = pygame.image.load("C:/Users/Daulet/Downloads/min_hand.png")  
left_hand = pygame.image.load("C:/Users/Daulet/Downloads/sec_hand.png")  


def draw_hand(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, -angle)  
    rect = rotated_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))  
    screen.blit(rotated_image, rect.topleft)  


running = True
while running:
    screen.fill((255, 255, 255))  
    screen.blit(clock_face, (0, 0))  


    now = datetime.now()
    minutes = now.minute
    seconds = now.second

  
    minute_angle = (minutes % 60) * 6  # 
    second_angle = (seconds % 60) * 6  

    draw_hand(right_hand, minute_angle, WIDTH // 2, HEIGHT // 2)  # Правая рука = минуты
    draw_hand(left_hand, second_angle, WIDTH // 2, HEIGHT // 2)  # Левая рука = секунды

    pygame.display.flip()  

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time.sleep(1) 

pygame.quit()
