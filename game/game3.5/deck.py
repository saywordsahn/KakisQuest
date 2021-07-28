import pygame
from cards.card import *

from card_sprites import CardSprites

class Deck:

    def __init__(self, game):
        self.cards = CardSprites('sprites/cards.png', 32, 48)
        self.game = game
        colorKey = pygame.Color('Black')
        attackCardImage = self.cards.get_image_at_index(0, colorKey)
        defendCardImage = self.cards.get_image_at_index(1, colorKey)
        fishCardImage = self.cards.get_image_at_index(2, colorKey)

        card_y_pos = game.settings.screen_width - game.settings.card_height_pixels
        card_x_start = 200
        a = AttackCard(attackCardImage, game.screen, card_x_start, card_y_pos)
        d = DefendCard(defendCardImage, game.screen, card_x_start + 32, card_y_pos)
        f = FishCard(fishCardImage, game.screen, card_x_start + 64, card_y_pos)
        self.card_sprites = pygame.sprite.Group(a, d, f)
        self.cards = [a, d, f]

    def draw_hand(self):
        self.card_sprites.draw(self.game.screen)
