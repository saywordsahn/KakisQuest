import pygame
from settings import Settings
from player import Player
from npc import Npc

class Game:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, create resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.clock = pygame.time.Clock()

        self.player = Player('sprites/kaki.png', 30, 30)

        self.slime1 = Npc('sprites/slime.png', 350, 30)
        self.all_players = pygame.sprite.Group(self.slime1, self.player)
        self.enemies = pygame.sprite.Group(self.slime1)


    def run_game(self):
        """Start the main loop of the game"""
        while True:
            self._check_events()
            self._update_screen()


    def _check_events(self):
        collide = pygame.sprite.spritecollide(self.player, self.enemies, False)
        print(collide)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        keys = pygame.key.get_pressed()
        self.player.process_events(keys)

    def _update_screen(self):

        self.all_players.draw(self.screen)
        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(self.settings.fps)

        self.screen.fill(0)


if __name__ == '__main__':
    game = Game()
    game.run_game()