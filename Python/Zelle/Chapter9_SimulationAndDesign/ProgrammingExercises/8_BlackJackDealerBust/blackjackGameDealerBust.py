# blackjackGameDealerBust.py
# A program that simulates multiple games of blackjack and estimates the
# probability the dealer will bust.
"""Blackjack (twenty-one) is a casino game played with cards. The goal of the
game is to draw cards that total as close to 21 points as possible without 
going over. All face cards count as 10 points, aces count as 1 or 11, and all
other cards count their numeric value.
    The game is played against a dealer. The player tries to get closer to 21
(without goint over) than the dealer. If the dealer busts (goes over 21), the 
player automatically wins (provided the player had not already busted). The 
dealer must always take cards according to a fixed set for rules. The dealer 
takes cards until he or she achieves a total of at least 17. If the dealer's 
hand contains an ace, it will be counted as an 11 when that results in a total
between 17 and 21 inclusive; otherwise, the ace is counted as 1.
    Write a program that simulates multiple games of blackjack and estimates
the probability that the dealer will bust. Hints: Treat the deck of cards as
infinite (casinos use a "shoe" containing many decks). You do not need to keep
track of the cards in the hand, just the total so far (treating an ace as a 1)
and a bool variable hasAce that tells whether or not the hand contains an ace. 
A hand containing an ace should have 10 points added to the total exactly when
doing so would produce a stopping total (something between 17 and 21 
inclusive)."""

from random import randrange

def main():

    printIntro()
    n = getInputs()
    busts = simNHands(n)
    printSummary(busts, n)

def printIntro():
    print("This game simulates a dealer playing hands of Blackjack. The dealer \
must hold at a hand of 17 and busts at a hand over 21. Aces are treated as 11 \
if it brings the hand to a score between 17 and 21. Otherwise aces are worth \
one.")

def getInputs():
    n = 0
    while n < 1:
        try:
            n = int(input("How many hands of Blackjack to simulate? "))
        except (SyntaxError, NameError, TypeError, ValueError):
            print("You have to enter a whole number.")
            continue
        if n < 1:
            print("You have to simulate at least one game.")
            continue
    return n

def simNHands(n):
    # Simulates n hands of blackjack
    busts = 0
    for i in range(n):
        bust = simOneHand()
        if bust == True:
            busts = busts + 1
    return busts

def simOneHand():
    # Simulates one hand of blackjack for the dealer.
    # The deck will be treated as infinite.

    # Use a list to keep track of drawn cards.
    cards = []

    # initial two card draw
    for i in range(2):
        drawCard = randrange(1, 11)
        cards.append(drawCard)

    inHand = scoreHand(cards)

    while not handOver(inHand):
    # check for greater than or equal to 17 or over 21
    # if less than 17, draw again
    # else hold
        drawCard
        cards.append(drawCard)
        inHand = scoreHand(cards)

    if inHand > 21:
        bust = True
    else:
        bust = False

    return bust

def scoreHand(cards):
    # Initialize the score of the hand and check for an ace.
    score = 0        
    for i in cards:
        if i == 1 or i == 11:
            hasAce = True
            if i == 1:
                cards.remove(1)
                ace = 11
                cards.append(ace)
        else:
            hasAce = False

    # Score the hand treating ace as 11
    for j in range(len(cards)):
        score = score + cards[j]

    # Check for bust and reduce the ace to one if true.
    if hasAce == True and score > 21:
        cards.remove(11)
        ace = 1
        cards.append(ace)

    # Rescore the hand
    score = 0
    for k in range(len(cards)):
        score = score + cards[k]

    return score

def handOver(inHand):
    # The dealer stops drawing if his hand scores over 17 regardless of busting
    if inHand >= 17:
        return True
    else:
        return False

def printSummary(busts, n):
    # Prints a summary of busted hands and the percentage of busted hands

    print("\nHands simulated:", n)
    print("The dealer had {0} busted hands with a player win percentage of \
({1:0.1%}).".format(busts, busts/n))

if __name__ == '__main__': main()
