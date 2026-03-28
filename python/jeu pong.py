#===================================
#Luhan.K / 2025
#===================================
import pygame
import random
import sys

pygame.init()

# Fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de Tir")

clock = pygame.time.Clock()

# Couleurs
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
BLACK = (0, 0, 0)

# Joueur
player = pygame.Rect(370, 500, 60, 60)
player_speed = 6

# Listes
bullets = []
enemies = []

score = 0
font = pygame.font.Font(None, 40)

enemy_timer = 0

running = True
while running:
    clock.tick(60)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(player.centerx - 5, player.y, 10, 20)
                bullets.append(bullet)

    keys = pygame.key.get_pressed()

    # Déplacement joueur
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed

    # Apparition ennemis
    enemy_timer += 1
    if enemy_timer > 30:
        enemy = pygame.Rect(random.randint(0, WIDTH - 50), 0, 50, 50)
        enemies.append(enemy)
        enemy_timer = 0

    # Mouvement balles
    for bullet in bullets[:]:
        bullet.y -= 10
        if bullet.bottom < 0:
            bullets.remove(bullet)

    # Mouvement ennemis
    for enemy in enemies[:]:
        enemy.y += 3
        if enemy.top > HEIGHT:
            enemies.remove(enemy)

    # Collisions
    for enemy in enemies[:]:
        for bullet in bullets[:]:
            if enemy.colliderect(bullet):
                enemies.remove(enemy)
                bullets.remove(bullet)
                score += 1
                break

        if enemy.colliderect(player):
            running = False

    # Dessin
    pygame.draw.rect(screen, BLUE, player)

    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)

    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()
