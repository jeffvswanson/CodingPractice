# randomPlayingCardGenerator.py
# A program that prints out n randomly generated cards and the associated
# BlackJack value where n is a number supplied by the user.
"""Implement a class to represent a playing card. Your class should have the 
following methods:
__init__(self, rank, suit) rank is an int in the range 1-13 indicating the 
    ranks ace-king, and suit (diamonds, clubs, hearts, or spades). Create the
    corresponding card.
getRank(self) Returns the rank of the card.
getSuit(self) Returns the suit of the card.
value(self) Returns the Blackjack value of a card. Ace counts as 1, face cards
    count as 10.
__str__(self) Returns a string that names the card. For example, "Ace of 
    Spades".
Note: A method names __str__ is special in Python. If asked to convert an 
object into a string, Python uses this method, if it's present. For example,
c = Card(1,"s")
print c

will print "Ace of Spades."
    Test your card class with a program that prints out n randomly generated
cards and the associated Blackjack value where n is a number supplied by the
user."""

from random import randrange

from playingCardClass import playingCard

def main():

    print("This program allows you to generate random playing cards and \
prints the name of the card and its associated Blackjack value.")

    suitList = ["c", "d", "h", "s"]
    n = 0
    while n <= 0:
        try:
            n = int(input("Please enter the number of cards you want randomly \
displayed: "))
            if n <= 0:
                print("You have to enter a number greater than zero.")
        except(SyntaxError, NameError, TypeError, ValueError):
            print("You have to enter a number greater than zero.")
            continue

    # Loop through the number of cards entered by the user and randomly create 
    # cards
    for card in range(0, n-1):
        rank = randrange(1, 13)
        j = randrange(0, 3)
        suit = suitList[j]
        card = playingCard(rank, suit)
        print("The card is: {0} and its BlackJack value is {1}"
        .format(card.__str__(), card.BJValue().__str__()))
            
main()
