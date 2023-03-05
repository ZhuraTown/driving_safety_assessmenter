import math
import pygame
from pygame import Vector2
from auto_racing.utils import scale_image


class Car(pygame.sprite.Sprite):
    COEFFICIENT_TO_VELOCITY = 15
    COEFFICIENT_SCALE = 0.55

    def __init__(self, x, y, max_vel_forward, max_vel_backward, rotation_vel):
        super().__init__()
        self.image = scale_image(pygame.image.load('imgs/red-car.png'), self.COEFFICIENT_SCALE)
        self.max_vel = max_vel_forward / self.COEFFICIENT_TO_VELOCITY
        self.max_vel_backward = max_vel_backward / self.COEFFICIENT_TO_VELOCITY

        self.vel = 0
        self.angle = 0
        self.rotation_vel = rotation_vel
        self.x, self.y = x, y

        self.acceleration_forward = 0.07
        self.acceleration_backward = 0.05
        self.acceleration_braking_inertia = 0.04
        self.acceleration_of_braking = 0.11
        self.braking_press = False

    def get_velocity_km_h(self):
        return self.vel * self.COEFFICIENT_TO_VELOCITY

    @staticmethod
    def blit_rotate_center(win, image, top_left, angle):
        rotated_image = pygame.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
        win.blit(rotated_image, new_rect.topleft)

    def reduce_speed(self):
        if self.vel > 0:
            self.vel = max(self.vel - self.acceleration_braking_inertia / 2, 0)
        if self.vel < 0:
            self.vel = min(self.vel + self.acceleration_braking_inertia / 2, 0)
        self.move()

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win):
        self.blit_rotate_center(win, self.image, (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration_forward, self.max_vel)
        self.move()

    def move_backward(self):
        self.vel = max(self.vel - self.acceleration_backward, -self.max_vel_backward)
        self.move()

    def braking(self):
        if self.vel > 0:
            self.vel = min(self.vel - self.acceleration_of_braking, self.max_vel)
        if self.vel < 0:
            self.vel = max(self.vel + self.acceleration_of_braking, -self.max_vel_backward)

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel
        self.y -= vertical
        self.x -= horizontal

    def collide(self, mask, x=0, y=0):
        car_mask = pygame.mask.from_surface(self.image)
        offset = (int(self.x - x), int(self.y - y))
        poi = mask.overlap(car_mask, offset)
        return poi

    def move_player(self):
        keys = pygame.key.get_pressed()
        moved = False
        self.braking_press = False

        if keys[pygame.K_a]:
            self.rotate(left=True)
        if keys[pygame.K_d]:
            self.rotate(right=True)
        if keys[pygame.K_w]:
            moved = True
            self.move_forward()
        if keys[pygame.K_s]:
            moved = True
            self.move_backward()

        if keys[pygame.K_SPACE] and not moved:
            self.braking()
            self.braking_press = True

        if not moved:
            self.reduce_speed()
