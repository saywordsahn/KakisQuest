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
        card_y_pos = game.settings.screen_width - game.settings.card_height_pixels
        card_x_start = 200
        a = Card(attackCardImage, game.screen, card_x_start, card_y_pos)
        d = Card(defendCardImage, game.screen, card_x_start + 32, card_y_pos)
        f = Card(fishCardImage, game.screen, card_x_start + 64, card_y_pos)
        self.cards = [a, d, f]

    def draw_hand(self):
        for card in self.cards:
            card.blitme()
