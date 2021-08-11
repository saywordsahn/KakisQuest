import pygame
from slimeType import SlimeType
class Npc(pygame.sprite.Sprite):

    def __init__(self, image, x, y, slime_type, screen_width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(x=x, y=y)
        self.vel = 1
        self.slime_type = SlimeType(slime_type)
        self.screen_width = screen_width
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
        else:
            if self.rect.left + self.vel < 0:
                self.rect.left = 0
                self.vel = self.vel * -1
            elif self.rect.right + self.vel > self.screen_width:
                self.rect.right = self.screen_width
                self.vel = self.vel * -1
            else:
                self.rect.move_ip(self.vel, 0)