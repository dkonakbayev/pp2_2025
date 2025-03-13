import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)


ball_radius = 25
ball_x = WIDTH // 2  # по центру экрана
ball_y = HEIGHT // 2
speed = 20  # на сколько пикселей передвигать шар


running = True
while running:
    pygame.time.delay(50)  

   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()

    
    if keys[pygame.K_LEFT] and ball_x - ball_radius - speed >= 0:
        ball_x -= speed
    if keys[pygame.K_RIGHT] and ball_x + ball_radius + speed <= WIDTH:
        ball_x += speed
    if keys[pygame.K_UP] and ball_y - ball_radius - speed >= 0:
        ball_y -= speed
    if keys[pygame.K_DOWN] and ball_y + ball_radius + speed <= HEIGHT:
        ball_y += speed

 
    screen.fill(WHITE)  
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)  
    pygame.display.update()  

pygame.quit()
