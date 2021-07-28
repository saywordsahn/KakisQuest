# add gui class with some text

import pygame
from settings import Settings
from kaki import Kaki
from slime import Slime
from background import Background
from game_state import GameState
from battle import Battle
from gui import GUI

class Game:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, create resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Kaki's Quest")
        self.clock = pygame.time.Clock()
        self.bg = Background()
        self.player = Kaki('sprites/kaki.png', 30, 30)
        self.slime1 = Slime('sprites/slime.png', 350, 30)
        self.all_players = pygame.sprite.Group(self.slime1, self.player)
        self.enemies = pygame.sprite.Group(self.slime1)

        self.GUI = GUI(self)

        self.game_state = GameState.MAP
        self.battle = None

    def run_game(self):
        """Start the main loop of the game"""
        while True:
            self._check_collisions()
            self._check_events()
            self._update_screen()

    def _check_collisions(self):
        collide = pygame.sprite.spritecollide(self.player, self.enemies, False)
        for collision in collide:
            if collision in self.enemies:
                self.battle = Battle(self.player, collision)
                self.game_state = GameState.BATTLE
                return

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        keys = pygame.key.get_pressed()
        if self.game_state == GameState.MAP:
            self.player.process_events(keys, self.clock.get_time())
            self.enemies.update(self.player)
        else:
            pass

    def _update_screen(self):
        if self.game_state == GameState.MAP:
            self.all_players.draw(self.screen)
        else:
            self.GUI.drawGUI()

        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(self.settings.fps)
        self.screen.fill(0)


if __name__ == '__main__':
    game = Game()
    game.run_game()