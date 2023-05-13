import unittest
from deck import Deck
            
class TestDeck(unittest.TestCase):
        
    def test_deal(self):
        d1 = Deck()
        d1.shuffle()
        d2 = Deck()
        num_matches = 0
        for i in range(0, 52):
            if d1.cards[i] == d2.cards[i]:
                num_matches += 1
        self.assertLess(num_matches, 5, "deck doesn't look shuffled well matches: " + str(num_matches))
        
unittest.main()