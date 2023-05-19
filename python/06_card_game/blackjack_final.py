from card import *
from deck import *

def score_hand(cards):
    score = 0
    have_ace = False
    for card in cards:
        if card.is_ace():
            have_ace = True
        score += card.value()
        if score > 21 and have_ace:
            score -= 10 # lower ace value
            have_ace = False # only do this once
    return score

def display_hand(hand):
    score = score_hand(hand)
    print('Your hand: ' + str(hand) + ' (' + str(score) + ')')

def play_game():
    deck = Deck()
    deck.shuffle()
    hand = []
    deck.deal(2, hand)
    print('\n\nNew Game')
    
    while True:
        score = score_hand(hand)
        display_hand(hand)
        action = input('t-twist or s-stick: ')
        if action == 't':
            deck.deal(1, hand)
            score = score_hand(hand)
            if score > 21:
                display_hand(hand)
                print('BUST!')
                break
        elif action == 's':
            print('Sticking with :' + str(score))
            break
    
while True:
    play_game()
