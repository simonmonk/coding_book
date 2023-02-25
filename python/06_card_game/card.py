class Card:
    
    clubs = '\u2663'
    spades = '\u2665'
    hearts = '\u2661'
    diamonds = '\u2662'
    possible_suits = [clubs, spades, hearts, diamonds]
    
    possible_pips = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, pips, suit):
        self.pips = pips
        self.suit = suit
    
    def __repr__(self):
        return self.pips + self.suit
    
    def value(self):
        if self.pips == 'A': # Ace defaults to 11
            return 11
        elif self.pips in ('J', 'Q', 'K'):
            return 10
        else:
            return int(self.pips)
        
    def is_ace(self):
        return (self.pips == 'A')