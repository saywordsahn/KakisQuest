import pygame
from spritesheet import SpriteSheet

class CardSprites(SpriteSheet):

    def __init__(self, image, card_width, card_height):
        SpriteSheet.__init__(self, image)
        self.card_width = card_width
        self.card_height = card_height

    def get_image_at_index(self, index, colorkey):
        # Loads image from x, y, x+offset, y+offset.
        rect = pygame.Rect((0, self.card_height * index, self.card_width, self.card_height))
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
