from Card import *

class Hand(object):
    """Creates a hand of cards"""

    def __init__(self):
        self.cards = []

    def __str__(self):
        if len(self.cards) == 0:
            info = "Empty hand!"
        else:
            info = ""
            counter = 0
            for i in self.cards:
                info += str(i.value) + " " + str(i.suit) + "    "
                counter += 1
                if counter % 10 == 0:
                    info += "\n"
            info += "\n"
        return info

    def addCard(self, card:Card):
        self.cards.append(card)

    def clearHand(self):
        self.cards = []

    def giveCard(self, card:Card, otherHand):
        """This will take one card from the current hand and place it in another hand"""
        self.cards.remove(card)
        otherHand.cards.append(card)

card1 = Card(8, "H")
card2 = Card(10, "C")
card3 = Card("A", "H")
card4 = Card("Q", "D")
card5 = Card("K", "S")
card6 = Card(2, "H")
hand1 = Hand()
hand2 = Hand()
hand1.addCard(card1)
hand1.addCard(card2)
hand1.addCard(card3)
hand2.addCard(card4)
hand2.addCard(card5)
hand2.addCard(card6)
print(hand1)
print(hand2)

hand1.giveCard(card2, hand2)

print(hand1)
print(hand2)

hand1.clearHand()

print(hand1)
