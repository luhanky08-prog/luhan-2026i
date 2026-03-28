
#===================================
#Luhan.K / 2025
#===================================


import pygame
import random

pygame.init()

# Fenêtre
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de tir 2D")

# Couleurs
WHITE = (255, 255, 255)
RED = (255, 50, 50)
BLUE = (50, 150, 255)
BLACK = (0, 0, 0)

# Joueur
player = pygame.Rect(WIDTH//2 - 25, HEIGHT - 60, 50, 50)
player_speed = 5

# Balles
bullets = []
bullet_speed = 7

# Ennemi
enemy = pygame.Rect(random.randint(0, WIDTH-50), -50, 50, 50)
enemy_speed = 3

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)
    screen.fill(BLACK)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(pygame.Rect(player.centerx - 5, player.y, 10, 20))

    # Déplacement joueur
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed

    # Déplacement balles
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

    # Déplacement ennemi
    enemy.y += enemy_speed
    if enemy.y > HEIGHT:
        enemy.x = random.randint(0, WIDTH-50)
        enemy.y = -50

    # Collision
    for bullet in bullets[:]:
        if enemy.colliderect(bullet):
            bullets.remove(bullet)
            enemy.x = random.randint(0, WIDTH-50)
            enemy.y = -50

    # Dessin
    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, RED, enemy)

    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)

    pygame.display.flip()

pygame.quit()