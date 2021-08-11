import pygame
import random
from settings import Settings
from slimeType import SlimeType
class Npc(pygame.sprite.Sprite):

    def __init__(self, image, x, y, slime_type, settings: Settings):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(x=x, y=y)
        self.slime_type = slime_type
        print(self.slime_type)
        if slime_type == SlimeType.FOLLOW:
            self.vel = 1
        else:
            self.vel = random.choice([-1, 1])
        self.screen_width = settings.screen_width
        self.screen_height = settings.screen_height
        print(self.slime_type)

    def update(self, player):
        if self.slime_type == SlimeType.FOLLOW:
            if self.rect.centerx > player.rect.centerx:
                self.rect.move_ip(-self.vel, 0)
            if self.rect.centerx < player.rect.centerx:
                self.rect.move_ip(self.vel, 0)
            if self.rect.centery > player.rect.centery:
                self.rect.move_ip(0, -self.vel)
            if self.rect.centery < player.rect.centery:
                self.rect.move_ip(0, self.vel)
        elif self.slime_type == SlimeType.HORIZONTAL:
            if self.rect.left + self.vel < 0:
                self.rect.left = 0
                self.vel = self.vel * -1
            elif self.rect.right + self.vel > self.screen_width:
                self.rect.right = self.screen_width
                self.vel = self.vel * -1
            else:
                self.rect.move_ip(self.vel, 0)
        else:
            if self.rect.top + self.vel < 0:
                self.rect.top = 0
                self.vel = self.vel * -1
            elif self.rect.bottom + self.vel > self.screen_height:
                self.rect.bottom = self.screen_height
                self.vel = self.vel * -1
            else:
                self.rect.move_ip(0, self.vel)