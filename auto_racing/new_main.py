import pygame
import sys
from auto_racing.car import Car
from auto_racing.debug import debug

WIDTH = 1280
HEIGHT = 720
FPS = 60


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("АвтоСимулятор")
        self.clock = pygame.time.Clock()
        position_car = 100, 100
        self.car = Car(*position_car, 120, 35, 2)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(color=(0,0,0))
            self.car.draw(self.screen)
            self.car.move_player()

            debug(f"Скорость: {self.car.get_velocity_km_h()}")
            debug(f"Тормоз: {'Нажат' if self.car.braking_press else ' '}", 40, 10)

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
