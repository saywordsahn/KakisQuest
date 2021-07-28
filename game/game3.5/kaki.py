import pygame
from spritesheet import SpriteSheet
from deck import Deck

class Kaki(pygame.sprite.Sprite):

    def __init__(self, image, x, y, deck):
        pygame.sprite.Sprite.__init__(self)
        sheet = SpriteSheet(image)
        self.imgs = sheet.load_strip((0, 0, 21, 29), 2)
        self.current_img = 0
        self.image = self.imgs[self.current_img]
        self.rect = self.imgs[0].get_rect(x=x, y=y)
        self.player_vel = 4
        self.frame_index = 0
        self.animation_speed = .05
        self.health = 100
        self.deck = deck
        for image in self.imgs:
            image.set_colorkey(pygame.Color('black'))



    def process_events(self, keys, frames):

        if self.frame_index >= len(self.imgs):
            self.frame_index = 0

        self.image = self.imgs[int(self.frame_index)]
        self.frame_index += self.animation_speed

        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.player_vel, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.player_vel, 0)
        if keys[pygame.K_UP]:
            self.rect.move_ip(0, -self.player_vel)
        if keys[pygame.K_DOWN]:
            self.rect.move_ip(0, self.player_vel)