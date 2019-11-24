import pygame
import random
import math
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
alienX = random.randint(0, 735)
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

score = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


def alien(x, y):
    screen.blit(alienImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(alienX, alienY, bulletX, bulletY):
    distance = math.sqrt((math.pow(alienX-bulletX, 2)) + (math.pow(
        alienY-bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


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
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    # Get the current X coordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
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
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Collision
    collision = isCollision(alienX, alienY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        alienX = random.randint(0, 735)
        alienY = random.randint(50, 150)

    player(playerX, playerY)
    alien(alienX, alienY)
    pygame.display.update()
