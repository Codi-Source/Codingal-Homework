
import pygame

# Screen Settings
width, height = 2000, 800
screen = pygame.display.set_mode((width, height))

# Color
WHITE = (255, 255, 255)

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    pygame.display.flip()

pygame.quit()
sys.exit()