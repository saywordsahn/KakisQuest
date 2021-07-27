# testing collisions
import pygame

# Game info
pygame.init()
screen_width, screen_height = 640, 480
screen=pygame.display.set_mode((screen_width, screen_height))
FPS = 60
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):

    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(x=x, y=y)



player = Player('kaki.png', 30, 30)
player_vel = 2

slime1 = Player('slime.png', 350, 30)
all_players = pygame.sprite.Group(slime1, player)
enemies = pygame.sprite.Group(slime1)


# 4 - keep looping through
while True:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    collide = pygame.sprite.spritecollide(player, enemies, False)
    print(collide)

    # 8 - loop through the events
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

    all_players.draw(screen)
    pygame.display.flip()
    pygame.display.update()
    clock.tick(FPS)