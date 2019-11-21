import pygame

# Init Pygame
pygame.init()

# Screen creation
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('space-invaders.png')
pygame.display.set_icon(icon)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = Falses
    screen.fill((0, 0, 0))
    pygame.display.update()
