# 1 - Import library
import pygame
from pygame.locals import *

# Game info
pygame.init()
screen_width, screen_height = 640, 480
screen=pygame.display.set_mode((screen_width, screen_height))
FPS = 60
clock = pygame.time.Clock()

# Player
player_vel = 1
player_x = 100
player_y = 100
player_sprite = pygame.image.load("kaki.png")

# Slime
enemy_sprite = pygame.image.load("slime.png")
enemy_x = 350
enemy_y = 350

# 3 - Load images


# 4 - keep looping through
while True:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    screen.blit(player_sprite, (player_x, player_y))
    screen.blit(enemy_sprite, (enemy_x, enemy_y))
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_vel
    if keys[pygame.K_RIGHT]:
        player_x += player_vel
    if keys[pygame.K_UP]:
        player_y -= player_vel
    if keys[pygame.K_DOWN]:
        player_y += player_vel

    clock.tick(FPS)