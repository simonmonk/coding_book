from card import *
from deck import *

def play_game():
    deck = Deck()
    deck.shuffle()
    hand = []
    deck.deal(2, hand)
    while True:
        print(hand)
        action = input('t-twist or s-strick: ')
        if action == 't':
            deck.deal(1, hand)
        elif action == 's':
            print('Sticking')
            break
    
play_game()