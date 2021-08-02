import pygame

class Npc(pygame.sprite.Sprite):

    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(x=x, y=y)
        self.vel = 1

    def update(self, player):
        if self.rect.centerx > player.rect.centerx:
            self.rect.move_ip(-self.vel, 0)
        if self.rect.centerx < player.rect.centerx:
            self.rect.move_ip(self.vel, 0)
        if self.rect.centery > player.rect.centery:
            self.rect.move_ip(0, -self.vel)
        if self.rect.centery < player.rect.centery:
            self.rect.move_ip(0, self.vel)