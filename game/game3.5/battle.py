
class Battle():

    def __init__(self, player, enemy):
        self.is_players_turn = True
        self.player = player
        self.enemy = enemy


    def process_play_card(self, card):
        self.is_players_turn = False
        if card.name == 'Attack':
            self.enemy.health -= card.damage
        elif card.name == 'Defend':
            pass
        else:
            pass

        self.enemy_turn()

    def enemy_turn(self):
        self.player.health -= 1
        self.is_players_turn = True


