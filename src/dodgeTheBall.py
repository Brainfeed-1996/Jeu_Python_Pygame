"""
Ce module fournit des fonctions pour générer un jeu Python avec un personnage et des balles. Le personnage peut être déplacé horizontalement à l'aide des touches gauche et droite du clavier. Des balles apparaissent aléatoirement en haut de l'écran et tombent. Si une balle touche le personnage, le jeu se termine. Le jeu continue tant que le personnage n'est pas touché par une balle.
"""

from random import randint
import pygame
import sys

print(pygame.ver)
pygame.init()

fenetre = pygame.display.set_mode((640, 460), pygame.RESIZABLE)

from balle import Balle

pygame.key.set_repeat(400, 30)

fond = pygame.image.load("background.jpg").convert()
perso = pygame.image.load("Perso.png").convert_alpha()
persoRect = perso.get_rect()
persoRect.topleft = (270, 380)
fenetre.blit(fond, (0, 0))

continuer = True
listeBalles = []
balle_group = pygame.sprite.Group()

while continuer:
    if len(listeBalles) < 10 and randint(1, 500) <= 10:
        balle = Balle('golfBall.png', (randint(25, 455), -25))
        listeBalles.append(balle)
        balle_group.add(balle)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if persoRect.left >= 10:
                    persoRect = persoRect.move(-10, 0)
            elif event.key == pygame.K_RIGHT:
                if persoRect.right <= 630:
                    persoRect = persoRect.move(10, 0)

    fenetre.blit(fond, (0, 0))
    balle_group.update()
    for ball in listeBalles:
        if ball.rect.top >= 480:
            listeBalles.remove(ball)
            balle_group.remove(ball)
        else:
            if ball.rect.colliderect(persoRect):
                continuer = False
        ball.affiche(fenetre)

    fenetre.blit(perso, persoRect)
    pygame.display.update()
    pygame.time.wait(10)

pygame.quit()
sys.exit()
