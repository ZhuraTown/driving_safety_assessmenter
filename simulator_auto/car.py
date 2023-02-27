import pygame

class Car(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('files/car.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
