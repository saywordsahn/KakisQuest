import pygame

class Card(pygame.sprite.Sprite):

    def __init__(self, image, screen, x, y):
        self.image = image
        self.screen = screen
        self.x, self.y = x, y


    def blitme(self):
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.screen.blit(self.image, self.rect)