import pygame
from spritesheet import SpriteSheet

class Gun(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.right_x_offset = 7
        self.right_y_offset = 13
        self.image = pygame.image.load('sprites/gun.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x + self.right_x_offset
        self.rect.y = y + self.right_y_offset
        self.cooldown = 500
        self.timer = pygame.time.get_ticks()


    def can_shoot(self):
        return pygame.time.get_ticks() - self.timer > self.cooldown

    def shoot(self):
        self.timer = pygame.time.get_ticks()
        print('shoot')

    def update_pos(self, x, y):
        self.rect.x = x + self.right_x_offset
        self.rect.y = y + self.right_y_offset
