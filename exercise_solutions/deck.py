from card import Card
from random import shuffle

class Deck:
    
    def __init__(self):
        self.cards = []
        for suit in Card.possible_suits:
            for pips in Card.possible_pips:
                self.cards.append(Card(pips, suit))
                
    def __repr__(self):
        return '<Deck: ' + str(self.cards) + '>'
                
    def shuffle(self):
        shuffle(self.cards)
        
    def deal(self, n, hand):
        for i in range(0, n):
            hand.append(self.cards.pop())