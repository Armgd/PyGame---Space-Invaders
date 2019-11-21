import pygame
import random
# Init Pygame
pygame.init()

# Screen creation
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('space-invaders.png')
pygame.display.set_icon(icon)

# Game Background
backgound = pygame.transform.scale(pygame.image.load('background-game.jpg'), (
    800, 600))
# Player
playerImg = pygame.transform.smoothscale(pygame.image.load('player.png'), (
 64, 64))
playerX = 370
playerY = 480
playerX_change = 0

# Alien
alienImg = pygame.transform.smoothscale(pygame.image.load('alien.png'), (
 64, 64))
alienX = random.randint(0, 800)
alienY = random.randint(50, 150)
alienX_change = 4
alienY_change = 40

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
# Ready - Can't see the bullet on screen
# Fire - Bullet Moving
bullet_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def alien(x, y):
    screen.blit(alienImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


# Game Loop
running = True
while running:
    # BKG fill
    screen.fill((0, 0, 0))
    screen.blit(backgound, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check keystroke L or R
        if event.type == pygame.KEYDOWN:
            print("Key pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Player Boundaries check
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Alien Boundaries check
    alienX += alienX_change

    if alienX <= 0:
        alienX_change = 4
        alienY += alienY_change
    elif alienX >= 736:
        alienX_change = -4
        alienY += alienY_change

    # Bullet Movement
    if bullet_state == "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    alien(alienX, alienY)
    pygame.display.update()
