#Author: Roshan Shivnani
#Date: 10/26/2026
#Purpose/Description: creates a deck class that can be randomly shuffled and delt
#File: deck.py
#Course: CS1

from random import randint
from card import Card

class Deck:
    #initial deck is empty list
    def __init__(self):
        self.card_list = []

    #add card adds 1-13 (all numbers) for 1-4 (all suites) which adds all cards to deck
    def add_standard_cards(self):
        for rank in range(1, 14):
            for suit in range(1, 5):
                self.card_list.append(Card(rank, suit))

    #deals a 'n' number of cards by popping them from the deck
    def deal(self, n):
        deal_hand = Deck()

        #for however many 'n' cards delt they get removed from initial list and added to hand = popping them
        for card in range(n):
            x = self.card_list.pop()
            deal_hand.card_list.append(x)

        return deal_hand

    #swaps two random cards in the deck a total number of the length of the decks times
    def shuffle(self):
        for i in range(len(self.card_list)):
            random_index = randint(0, len(self.card_list)-1)
            random_index2 = randint(0, len(self.card_list)-1)
            temp = self.card_list[random_index2]
            self.card_list[random_index2] = self.card_list[random_index]
            self.card_list[random_index] = temp
