import unittest
from deck import Deck
            
class TestDeck(unittest.TestCase):
        
    def test_deal(self):
        d = Deck()
        hand = []
        d.deal(1, hand)
        self.assertEqual(len(d.cards), 51, "incorrect deck size after dealing")
        self.assertEqual(len(hand), 1, "incorrect hand size after dealing")
        self.assertNotIn(hand[0], d.cards, "dealt card still in deck")
        
unittest.main()
