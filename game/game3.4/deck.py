import pygame
from card import Card
from card_sprites import CardSprites

class Deck:

    def __init__(self, game):
        self.cards = CardSprites('sprites/cards.png', 32, 48)
        colorKey = pygame.Color('Black')
        attackCardImage = self.cards.get_image_at_index(0, colorKey)
        defendCardImage = self.cards.get_image_at_index(1, colorKey)
        fishCardImage = self.cards.get_image_at_index(2, colorKey)
        a = Card(attackCardImage, game.screen, 0, 0)
        d = Card(defendCardImage, game.screen, 32, 0)
        f = Card(fishCardImage, game.screen, 64, 0)
        self.cards = [a, d, f]

    def draw_hand(self):
        for card in self.cards:
            card.blitme()
