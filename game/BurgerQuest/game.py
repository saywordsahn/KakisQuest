# make slime chase player if player
import pygame
import random

from slimeType import SlimeType
from settings import Settings
from player import Player
from npc import Npc
from background import Background
from burger import Burger

class Game:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, create resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.clock = pygame.time.Clock()
        self.bg = Background()
        self.font = pygame.font.Font(None, 28)
        self.player = Player('sprites/kaki.png', 30, 30)
        self.slime1 = Npc('sprites/slime.png', 350, 30, SlimeType.HORIZONTAL, self.settings)
        self.enemies = pygame.sprite.Group(self.slime1)
        self.gameOver = False

        self.burger = Burger('sprites/burger.png', 40, 100)
        self.burgers = pygame.sprite.Group(self.burger)
        self.spawnable_enemies = [SlimeType.HORIZONTAL, SlimeType.VERTICAL]

        self.all_players = pygame.sprite.Group(self.slime1, self.player, self.burger)

    def run_game(self):
        """Start the main loop of the game"""
        while True:
            self._check_collision()
            self._check_events()
            self._update_screen()


    def _check_collision(self):
        enemy_collide = pygame.sprite.spritecollide(self.player, self.enemies, False)
        burger_collide = pygame.sprite.spritecollide(self.player, self.burgers, False)

        if len(enemy_collide) > 0:
            self.player.health -= 1

        if len(burger_collide) > 0:
            self.player.burgers_eaten += 1
            self.burger.rect.x = random.randint(0, self.settings.screen_width)
            self.burger.rect.y = random.randint(0, self.settings.screen_height)
            if self.player.burgers_eaten % 1 == 0:
                randx = random.randint(0, self.settings.screen_width)
                randy = random.randint(0, self.settings.screen_height)
                random.seed(pygame.time.get_ticks())
                newSlime = Npc('sprites/slime.png', randx, randy, random.choice(self.spawnable_enemies), self.settings)
                self.all_players.add(newSlime)
                self.enemies.add(newSlime)

    def _check_events(self):

        if self.player.health <= 0:
            self.gameOver = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        keys = pygame.key.get_pressed()
        self.player.process_events(keys, self.clock.get_time(), self)
        self.enemies.update(self.player)

    def _draw_hud(self):
        text_color = pygame.color.Color('white')
        text = 'Burgers eaten: ' + str(self.player.burgers_eaten)
        txt_surface = self.font.render(text, True, text_color)

        health_txt = 'HP: ' + str(self.player.health)
        health_txt_surface = self.font.render(health_txt, True, text_color)
        self.screen.blit(txt_surface, (0, 0))
        self.screen.blit(health_txt_surface, (560, 0))

    def _update_screen(self):

        if not self.gameOver:
            self._draw_hud()
            self.all_players.draw(self.screen)
        else:
            pass
            game_over_text = 'GAME OVER'
            game_over_text_surface = self.font.render(game_over_text, True, pygame.color.Color('red'))
            self.screen.blit(game_over_text_surface, (self.settings.screen_width // 2, self.settings.screen_height // 2))

        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(self.settings.fps)
        self.screen.fill(0)




if __name__ == '__main__':
    game = Game()
    game.run_game()