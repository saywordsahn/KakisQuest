from card import Card
class DefendCard(Card):

    def __init__(self, image, screen, x, y):
        Card.__init__(self, image, screen, x, y)
        self.name = 'Defend'
        self.defense = 5
        self.desc = 'Blocks 5 damage'