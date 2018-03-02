class Card(object):
    """Creates and defines a card object"""

    def __init__(self, value, suit, isFaceUp = True):
        self.value = value
        self.suit = suit
        self.isFaceUp = isFaceUp

    def __str__(self):
        if self.isFaceUp == True:
            info = str(self.value) + " " + str(self.suit)
        else:
            info = "Unknown"
        return info

    def flipCard(self):
        """This flips cards from face-up to face-down or vice versa"""
        if self.isFaceUp == True:
            self.isFaceUp = False
        else:
            self.isFaceUp = True

# card = Card(9, "C", False)
# print(card)
# card.flipCard()
# print(card)
# card.flipCard()
# print(card)