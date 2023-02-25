import unittest
from deck import Deck
            
class TestDeck(unittest.TestCase):
    
    def test_init(self):
        d = Deck()
        self.assertEqual(len(d.cards), 52, "incorrect number of cards")
        
    def test_deal(self):
        d = Deck()
        hand = []
        d.deal(3, hand)
        self.assertEqual(len(d.cards), 49, "incorrect deck size after dealing")
        self.assertEqual(len(hand), 3, "incorrect hand size after dealing")
        
unittest.main()