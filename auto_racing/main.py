import pygame
import math
import sys

from utils import scale_image, blit_rotation_center

GRASS = scale_image(pygame.image.load("imgs/grass.jpg"), 2.5)
TRACK = scale_image(pygame.image.load('imgs/track.png'), 0.9)
TRACK_BORDER = scale_image(pygame.image.load('imgs/track-border.png'), 0.9)
FINISH = pygame.image.load('imgs/finish.png')
RED_CAR = scale_image(pygame.image.load('imgs/red-car.png'), 0.5)
GREEN_CAR = pygame.image.load('imgs/green-car.png')
WIDTH = TRACK.get_width()
HEIGHT = TRACK.get_height()
FPS = 60



# https://www.youtube.com/watch?v=L3ktUWfAMPg&ab_channel=TechWithTim

class AbstractCar:
    IMG = GREEN_CAR
    START_POS = (180, 200)

    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 90
        self.position_x, self.position_y = self.START_POS

    def rotate(self, left: bool = False, right: bool = False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, window):
        blit_rotation_center(window, self.img, (self.position_x, self.position_y), self.angle)


class PlayerCar(AbstractCar):
    IMG = RED_CAR


player_car = PlayerCar(4,4)
IMAGES = [(GRASS, (0,0)), (TRACK, (0,0))]


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("AutoRacing")
        self.clock = pygame.time.Clock()

    def draw(self, images,  car_user):
        for img, pos in images:
            self.screen.blit(img, pos)

        car_user.draw(self.screen)
        pygame.display.update()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # self.screen.blit(GRASS, (0,0))
            # self.screen.blit(TRACK, (0,0))
            # self.screen.blit(TRACK_BORDER, (0,0))
            self.draw(IMAGES, player_car)
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
