import pygame

class Card(pygame.sprite.Sprite):

    def __init__(self, image, screen, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.name = ''
        self.image = image
        self.screen = screen
        self.x, self.y = x, y
        self.rect = self.image.get_rect(x=x, y=y)


    def blitme(self):
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.screen.blit(self.image, self.rect)


class AttackCard(Card):

    def __init__(self, image, screen, x, y):
        Card.__init__(self, image, screen, x, y)
        self.name = 'Attack'
        self.damage = 5
        self.desc = 'Attack for 5 damage'


class DefendCard(Card):

    def __init__(self, image, screen, x, y):
        Card.__init__(self, image, screen, x, y)
        self.name = 'Defend'
        self.defense = 5
        self.desc = 'Blocks 5 damage'


class FishCard(Card):

    def __init__(self, image, screen, x, y):
        Card.__init__(self, image, screen, x, y)
        self.name = 'Fish'
        self.desc = 'This card smells...'