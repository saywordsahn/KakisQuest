from card import Card

class FishCard(Card):

    def __init__(self, image, screen, x, y):
        Card.__init__(self, image, screen, x, y)
        self.name = 'Fish'
        self.desc = 'This card smells...'