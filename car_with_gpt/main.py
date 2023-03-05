import pygame
import sys

WIDTH = 1280
HEIGHT = 720
FPS = 60

class Car(pygame.sprite.Sprite):
    pass


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

            # self.draw(IMAGES, player_car)
            # self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()