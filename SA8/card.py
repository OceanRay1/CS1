#Author: Roshan Shivnani
#Date: 10/26/2026
#Purpose/Description: creates a card class w/number & suite
#File: card.py
#Course: CS1

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

        #converts non-number values into ace/royalty
        if self.rank == 1:
            self.rank = "Ace"
        elif self.rank == 11:
            self.rank = "Jack"
        elif self.rank == 12:
            self.rank = "Queen"
        elif self.rank == 13:
            self.rank = "King"

    #adds cards suite w/1-4 corresponding to a suite
    def __str__(self):
        if self.suit == 4:
            return (str(self.rank) + " of hearts")
        elif self.suit == 3:
            return (str(self.rank) + " of spades")
        elif self.suit == 2:
            return (str(self.rank) + " of diamonds")
        else:
            return (str(self.rank) + " of clubs")
