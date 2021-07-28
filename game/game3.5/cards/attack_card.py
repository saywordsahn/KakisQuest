from card import Card

class AttackCard(Card):

    def __init__(self, image, screen, x, y):
        Card.__init__(self, image, screen, x, y)
        self.name = 'Attack'
        self.damage = 5
        self.desc = 'Attack for 5 damage'