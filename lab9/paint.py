import pygame
    
def main():
    pygame.init()

    # Настройки экрана и цвета
    width = 800
    height = 600
    white = (255, 255, 255)
    red = (255, 0, 0)
    black = (0, 0, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    green = (124, 252, 0)
    color = black

    # Инициализация экрана и слоя для рисования
    screen = pygame.display.set_mode((width, height))
    layer = pygame.Surface((width, height))
    clock = pygame.time.Clock()
    
    X, Y, x, y = -1, -1, -1, -1  # Координаты для рисования
    radius = 10  # Толщина линий

    screen.fill(white)
    layer.fill(white)
    
    isMouseDown = False  # Флаг зажатой кнопки мыши

    # Флаги режимов рисования
    drawLine = True
    drawRect = False
    drawCircle = False
    drawSquare = False
    drawRightTriangle = False
    drawEqualTriangle = False
    drawRhombus = False
    eraser = False

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                # Смена цвета кисти
                if event.key == pygame.K_1:
                    color = black
                if event.key == pygame.K_2:
                    color = red
                if event.key == pygame.K_3:
                    color = blue
                if event.key == pygame.K_4:
                    color = yellow
                if event.key == pygame.K_5:
                    color = green

                # Изменение размера кисти
                if event.key == pygame.K_UP and radius < 50:
                    radius += 3
                if event.key == pygame.K_DOWN and radius > 1:
                    radius -= 3
                
                # Выбор режима рисования
                drawRect = event.key == pygame.K_q
                drawCircle = event.key == pygame.K_w
                eraser = event.key == pygame.K_e
                drawLine = event.key == pygame.K_r
                drawSquare = event.key == pygame.K_a
                drawRightTriangle = event.key == pygame.K_s
                drawEqualTriangle = event.key == pygame.K_d
                drawRhombus = event.key == pygame.K_f

            # Обработка нажатий мыши
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    isMouseDown = True
                    x, y = event.pos
                    X, Y = event.pos
                
            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                layer.blit(screen, (0, 0))
    
            if event.type == pygame.MOUSEMOTION and isMouseDown:
                x, y = event.pos

        mouse = pygame.mouse.get_pos()
        
        # Режим рисования линий (кисть)
        if drawLine and pygame.mouse.get_pressed()[0]:
            pygame.draw.circle(screen, color, mouse, radius)
        
        # Режим рисования прямоугольников
        if isMouseDown and drawRect:
            screen.blit(layer, (0, 0))
            r = calculateRect(X, Y, x, y)
            pygame.draw.rect(screen, color, pygame.Rect(r), radius)
        
        # Режим рисования квадратов
        if isMouseDown and drawSquare:
            screen.blit(layer, (0, 0))
            yclon = x - X + Y
            r = calculateRect(X, Y, x, yclon)
            pygame.draw.rect(screen, color, pygame.Rect(r), radius)
        
        # Режим рисования окружностей
        if isMouseDown and drawCircle:
            screen.blit(layer, (0, 0))
            r = calculateRect(X, Y, x, y)
            pygame.draw.ellipse(screen, color, r, radius)
        
        # Режим рисования прямоугольного треугольника
        if isMouseDown and drawRightTriangle:
            screen.blit(layer, (0, 0))
            pygame.draw.polygon(screen, color, [[X, Y], [X, y], [x, y]], radius)
        
        # Режим рисования равностороннего треугольника
        if isMouseDown and drawEqualTriangle:
            screen.blit(layer, (0, 0))
            HEIGHT = y - Y
            WIDTH = x - X
            pygame.draw.polygon(screen, color, [(X, Y + HEIGHT), (x, y), (X + WIDTH / 2, Y)], radius)
        
        # Режим рисования ромба
        if isMouseDown and drawRhombus:
            screen.blit(layer, (0, 0))
            HEIGHT = y - Y
            WIDTH = x - X
            pygame.draw.polygon(screen, color, [(X, Y + HEIGHT / 2), (X + WIDTH/2, Y), (x, Y + HEIGHT/2), (X + WIDTH/2, y)], radius)
        
        # Ластик (замена цвета на белый)
        if eraser and pygame.mouse.get_pressed()[0]:
            pygame.draw.circle(screen, white, mouse, radius)
            
        pygame.display.flip()
        clock.tick(60)

# Функция вычисления прямоугольника по двум точкам
def calculateRect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))
    
main()
