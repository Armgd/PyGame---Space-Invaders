import pygame
from pygame import mixer
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

# Background Sound
mixer.music.load('background.wav')
mixer.music.play(-1)

# Player
playerImg = pygame.transform.smoothscale(pygame.image.load('player.png'), (
 64, 64))
playerX = 370
playerY = 480
playerX_change = 0

# Alien
alienImg = []
alienX = []
alienY = []
alienX_change = []
alienY_change = []
num_aliens = 6

for i in range(num_aliens):
    alienImg.append(pygame.transform.smoothscale(pygame.image.load(
        'alien.png'), (64, 64)))
    alienX.append(random.randint(0, 736))
    alienY.append(random.randint(50, 150))
    alienX_change.append(4)
    alienY_change.append(40)

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
# Ready - Can't see the bullet on screen
# Fire - Bullet Moving
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10


def show_score(x, y):
    score = font.render("score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


def alien(x, y, i):
    screen.blit(alienImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(alienX, alienY, bulletX, bulletY):
    distance = math.sqrt(math.pow(alienX - bulletX, 2) + (math.pow(
        alienY - bulletY, 2)))
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

    # Alien Movement
    for i in range(num_aliens):
        alienX[i] += alienX_change[i]

        if alienX[i] <= 0:
            alienX_change[i] = 4
            alienY[i] += alienY_change[i]
        elif alienX[i] >= 736:
            alienX_change[i] = -4
            alienY[i] += alienY_change[i]
        # Collision
        collision = isCollision(alienX[i], alienY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            print(score_value)
            alienX[i] = random.randint(0, 735)
            alienY[i] = random.randint(50, 150)

        alien(alienX[i], alienY[i], i)
    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
