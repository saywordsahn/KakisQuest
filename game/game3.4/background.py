import pygame
from spritesheet import SpriteSheet

class Background():

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        sheet = SpriteSheet('sprites/bg.png')
        self.imgs = sheet.load_strip((0, 0, 32, 32), 5)
