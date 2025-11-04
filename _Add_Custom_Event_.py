import pygame
import sys
# Screen Settings
width, height = 1000, 600
screen = pygame.display.set_mode((width, height))

# Color
WHITE = (255, 255, 255)
BLUE = (30, 144, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)

my_rect2 = pygame.Rect(400, 400, 300, 200)
my_rect2_color = BLACK
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        my_rect2_color = ORANGE
    else:
        my_rect2_color = BLACK
    

    # Rectangle Color
    
    pygame.draw.rect(screen, my_rect2_color, my_rect2)
    
    

    pygame.display.flip()

pygame.quit()
sys.exit()

