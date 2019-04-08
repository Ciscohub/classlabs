#!/usr/bin/env python3

from random import shuffle
# Blackjack game
print("Welcome to our blackjack game")
while True:
    # Need a horn of cards / dealer deck
    deck = [ "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K" ]
    suits = ["spades", "hearts", "clubs", "diamonds"]
    total_deck = []

    for suit in suits:
        for card in deck:
            total_deck.append(str(card) + "of" + suit) 

    print(len(total_deck))

    total_deck = total_deck * 6
    print(len(total_deck))

    shuffle(total_deck)
    print(total_deck)

    # Need a dealer hand
    # start with two cards
    # if total of hand < 16, do another hit
    dealer_hand = []
    
    # Need a player hand
    player_hand = []

    # Loop to keep game going until user says quit
    
    # Deal hands
    for x in range(2):
        dealer_hand.append(total_deck.pop())
        player_hand.append(total_deck.pop())
    
    print(dealer_hand[0], player_hand)



    while True:
        x = input("Do you want another card? ")
        if x.lower() == "y" or x.lower() == "yes":
            player_hand.append(total_deck.pop())
            print(player_hand)
        else:
            print(dealer_hand, player_hand)
            break
    # "Do you want to play again?"
    x = input(" Do you want to play again? ")
    if x.lower() == "n" or x.lower() == "no":
        break
