
import pygame

# Screen Settings
width, height = 1000, 600
screen = pygame.display.set_mode((width, height))

# Color
WHITE = (255, 255, 255)
BLUE = (30, 144, 255)
BLACK = (0, 0, 0)

# Rectangle Properties (x , y, width , hiehgt)
rect_x = 100
rect_y = 100
rect_w = 300
rect_h = 200
my_rect = pygame.Rect(rect_x,rect_y,rect_w, rect_h)
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Rectangle Color
    pygame.draw.rect(screen, BLUE, my_rect)

    # Border
    pygame.draw.rect(screen, BLACK, my_rect, 1)

    pygame.display.flip()

pygame.quit()
sys.exit()