import pygame

class Car(pygame.sprite.Sprite):

    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('files/car.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

        # self.direction = pygame.math.Vector2()
        self.direction = 0
        self.speed = 3
        self.angle = 0
        self.rotation_speed = 1.8
        self.obstacle_sprites = obstacle_sprites
        self.forward = pygame.math.Vector2(0, -1)

    def set_rotation(self):
        if self.direction == 1:
            self.angle -= self.rotation_speed
        if self.direction == -1:
            self.angle += self.rotation_speed

        self.image = pygame.transform.rotozoom(self.image, self.angle,  0.25)
        self.rect = self.image.get_rect(center=self.rect.center)

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_RIGHT:
                    self.direction += 1
                if event.type == pygame.K_LEFT:
                    self.direction -= 1
            if event.type == pygame.KEYUP:
                pass
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_UP]:
        #     self.direction.y = -1
        # elif keys[pygame.K_DOWN]:
        #     self.direction.y = 1
        # else:
        #     self.direction.y = 0
        #
        # if keys[pygame.K_RIGHT]:
        #     self.direction.x = 1
        # elif keys[pygame.K_LEFT]:
        #     self.direction.x = -1
        # else:
        #     self.direction.x = 0

    def move(self, speed):
        if self.direction.magnitude():
            self.direction = self.direction.normalize()

        self.rect.x += self.direction.x * speed
        self.collision("horizontal")
        self.rect.y += self.direction.y * speed
        self.collision("vertical")

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:  # move right
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:  # move left
                        self.rect.left = sprite.rect.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:  # move down
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:  # move up
                        self.rect.top = sprite.rect.bottom

    def update(self):
        # self.input()
        # self.set_rotation()
        # self.move(self.speed)
        self.set_rotation()