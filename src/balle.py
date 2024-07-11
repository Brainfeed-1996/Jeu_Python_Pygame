import pygame
from random import randint

class Balle(pygame.sprite.Sprite):
    def __init__(self, image, center):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect(center=center)
        self.vitesse = 5

    def update(self):
        self.rect.move_ip(0, self.vitesse)

    def affiche(self, fenetre):
        fenetre.blit(self.image, self.rect)
