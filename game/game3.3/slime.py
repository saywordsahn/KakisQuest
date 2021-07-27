import pygame

class Slime(pygame.sprite.Sprite):

    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(x=x, y=y)
        self.vel = 1
        self.aggro_distance = 80

    def update(self, player):

        if self.get_distance(player) <= self.aggro_distance:
            if self.rect.centerx > player.rect.centerx:
                self.rect.move_ip(-self.vel, 0)
            if self.rect.centerx < player.rect.centerx:
                self.rect.move_ip(self.vel, 0)
            if self.rect.centery > player.rect.centery:
                self.rect.move_ip(0, -self.vel)
            if self.rect.centery < player.rect.centery:
                self.rect.move_ip(0, self.vel)


    def get_distance(self, player):
        xdiff_squared = pow(player.rect.centerx - self.rect.centerx, 2)
        ydiff_squared = pow(player.rect.centery - self.rect.centery, 2)
        return pow(xdiff_squared + ydiff_squared, .5)