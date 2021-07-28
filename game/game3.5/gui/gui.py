import pygame
from deck import Deck

class GUI():

    def __init__(self, game):
        self.game = game
        self.selected_sprite = None

    def drawGUI(self):
        self.game.deck.draw_hand()

        white = pygame.Color('white')
        red = pygame.Color('red')
        green = pygame.Color('green')
        font = pygame.font.Font(None, 28)

        # character text
        text = 'Kaki'
        txt_surface = font.render(text, True, green)
        self.game.screen.blit(txt_surface, (0, 580))

        #health
        text = 'Health: ' + str(self.game.player.health)
        txt_surface = font.render(text, True, white)

        self.game.screen.blit(txt_surface, (0, 600))

        # character text
        text = 'Slime'
        txt_surface = font.render(text, True, red)
        self.game.screen.blit(txt_surface, (400, 0))

        # health
        text = 'Health: ' + str(self.game.slime1.health)
        txt_surface = font.render(text, True, white)

        self.game.screen.blit(txt_surface, (400, 20))



