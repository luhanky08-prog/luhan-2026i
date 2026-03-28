#===================================
#Luhan.K / 2025
#===================================
import pygame
import sys

pygame.init()

# Dimensions de la fenêtre
largeur = 800
hauteur = 600

fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Pong")

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Raquettes
raquette_largeur = 10
raquette_hauteur = 100

raquette_gauche = pygame.Rect(30, hauteur//2 - 50, raquette_largeur, raquette_hauteur)
raquette_droite = pygame.Rect(largeur - 40, hauteur//2 - 50, raquette_largeur, raquette_hauteur)

# Balle
balle = pygame.Rect(largeur//2 - 10, hauteur//2 - 10, 20, 20)
vitesse_balle_x = 10
vitesse_balle_y = 10

vitesse_raquette = 15

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    fenetre.fill(NOIR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Contrôles
    touches = pygame.key.get_pressed()
    if touches[pygame.K_q] and raquette_gauche.top > 0:
        raquette_gauche.y -= vitesse_raquette
    if touches[pygame.K_s] and raquette_gauche.bottom < hauteur:
        raquette_gauche.y += vitesse_raquette

    if touches[pygame.K_UP] and raquette_droite.top > 0:
        raquette_droite.y -= vitesse_raquette
    if touches[pygame.K_DOWN] and raquette_droite.bottom < hauteur:
        raquette_droite.y += vitesse_raquette

    # Déplacement balle
    balle.x += vitesse_balle_x
    balle.y += vitesse_balle_y

    # Rebonds haut/bas
    if balle.top <= 0 or balle.bottom >= hauteur:
        vitesse_balle_y *= -1

    # Collision raquettes
    if balle.colliderect(raquette_gauche) or balle.colliderect(raquette_droite):
        vitesse_balle_x *= -1

    # Si la balle sort
    if balle.left <= 0 or balle.right >= largeur:
        balle.center = (largeur//2, hauteur//2)

    # Dessin
    pygame.draw.rect(fenetre, BLANC, raquette_gauche)
    pygame.draw.rect(fenetre, BLANC, raquette_droite)
    pygame.draw.ellipse(fenetre, BLANC, balle)
    pygame.draw.aaline(fenetre, BLANC, (largeur//2, 0), (largeur//2, hauteur))

    pygame.display.flip()
