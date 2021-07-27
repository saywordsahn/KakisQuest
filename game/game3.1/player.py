import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(x=x, y=y)
        self.player_vel = 2


    def process_events(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.player_vel, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.player_vel, 0)
        if keys[pygame.K_UP]:
            self.rect.move_ip(0, -self.player_vel)
        if keys[pygame.K_DOWN]:
            self.rect.move_ip(0, self.player_vel)