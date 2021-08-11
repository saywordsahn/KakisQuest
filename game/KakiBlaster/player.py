import pygame
from spritesheet import SpriteSheet
from gun import Gun

class Player(pygame.sprite.Sprite):

    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        sheet = SpriteSheet(image)
        self.imgs = sheet.load_strip((0, 0, 21, 29), 2)
        self.current_img = 0
        self.image = self.imgs[self.current_img]
        self.rect = self.imgs[0].get_rect(x=x, y=y)
        self.player_vel = 2
        self.frame_index = 0
        self.animation_speed = .05
        self.burgers_eaten = 0
        self.health = 1000000
        for image in self.imgs:
            image.set_colorkey(pygame.Color('black'))

        self.gun = Gun(x, y)


    def process_events(self, keys, frames, game):

        if self.frame_index >= len(self.imgs):
            self.frame_index = 0

        self.image = self.imgs[int(self.frame_index)]
        self.frame_index += self.animation_speed

        if keys[pygame.K_LEFT]:
            if self.rect.x - self.player_vel <= 0:
                self.rect.x = 0
            else:
                self.rect.move_ip(-self.player_vel, 0)

        if keys[pygame.K_RIGHT]:
            if self.rect.right + self.player_vel >= game.settings.screen_width:
                self.rect.right = game.settings.screen_width
            else:
                self.rect.move_ip(self.player_vel, 0)
        if keys[pygame.K_UP]:
            if self.rect.top - self.player_vel <= 0:
                self.rect.top = 0
            else:
                self.rect.move_ip(0, -self.player_vel)

        if keys[pygame.K_DOWN]:
            if self.rect.bottom + self.player_vel >= game.settings.screen_height:
                self.rect.bottom = game.settings.screen_height
            else:
                self.rect.move_ip(0, self.player_vel)

        self.gun.update_pos(self.rect.x, self.rect.y)


        if keys[pygame.K_SPACE] and self.gun.can_shoot():
            self.gun.shoot()
            print('kaki pulls the trigger')
