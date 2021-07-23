# battle mode
import pygame

# Game info
pygame.init()
screen_width, screen_height = 640, 480
screen=pygame.display.set_mode((screen_width, screen_height))
FPS = 60
clock = pygame.time.Clock()


# Players
class Player(pygame.sprite.Sprite):

    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(x=x, y=y)


player = Player('kaki.png', 30, 30)
player_vel = 2

slime1 = Player('slime.png', 350, 30)
onscreen_chars = pygame.sprite.Group(slime1, player)
offscreen_chars = pygame.sprite.Group()
enemies = pygame.sprite.Group(slime1)

#text
font = pygame.font.Font(None, 32)
color = pygame.Color('white')
health = 100
txt_surface = font.render(str(health), True, color)
screen.blit(txt_surface, (50, 100))


# Scenes
battleMode = False

# 4 - keep looping through
while True:
    screen.fill(0)

    if not battleMode:
        # draw the screen elements
        collide = pygame.sprite.spritecollide(player, enemies, False)
        if len(collide) > 0:
            offscreen_chars = onscreen_chars.copy()
            onscreen_chars.empty()
            battleMode = True

        # loop through the events
        for event in pygame.event.get():
            # check if the event is the X button
            if event.type==pygame.QUIT:
                # if it is quit the game
                pygame.quit()
                exit(0)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player.rect.move_ip(-player_vel, 0)
        if keys[pygame.K_RIGHT]:
            player.rect.move_ip(player_vel, 0)
        if keys[pygame.K_UP]:
            player.rect.move_ip(0, -player_vel)
        if keys[pygame.K_DOWN]:
            player.rect.move_ip(0, player_vel)


    txt_surface = font.render(str(health), True, color)
    screen.blit(txt_surface, (0, 0))

    onscreen_chars.draw(screen)
    pygame.display.flip()
    pygame.display.update()

    clock.tick(FPS)