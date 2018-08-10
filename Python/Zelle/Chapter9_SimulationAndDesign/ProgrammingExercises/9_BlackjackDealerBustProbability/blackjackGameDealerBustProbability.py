# blackjackGameDealerBustCardFaceUp.py
# A program that simulates multiple games of blackjack and estimates the
# probability the dealer will bust knowing the value of the face up card.
"""A blackjack dealer always starts with one card showing. It would be useful
for a player to know the dealer's bust probability (see previous problem) for 
each possible starting value. Write a simulation program that runs multiple
hands of blackjack for each possible starting value (ace-10) and estimates the
probability that the dealer busts for each starting value."""

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
            n = int(input("How many hands of blackjack to simulate? "))
        except (SyntaxError, NameError, TypeError, ValueError):
            print("You have to enter a whole number.")
            continue
        if n < 1:
            print("You have to simulate at least one game.")
            continue
    return n

def simNHands(n):
    # Simulates n hands of blackjack at each card value

    # Create a list to store the number of busts for each value a face up card can be.
    busts = []
    for j in range(1, 11):
        numbusts = 0
        faceUpCard = j
        for i in range(n):
            bust = simOneHand(faceUpCard)
            if bust == True:
                numbusts = numbusts + 1
        busts.append(numbusts)
    return busts
    

def simOneHand(faceUpCard):
    # Simulates one hand of blackjack for the dealer.
    # The deck will be treated as infinite.

    # Use a list to keep track of drawn cards.
    cards = []

    # initial two card draw
    cards.append(faceUpCard)
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

    print("\nHands simulated per face-up card value:", n)
    for i in range (1, 11):
        if i == 1:
            print("The dealer had {0} busted hands with a player win \
percentage of ({1:0.1%}) when an ace was facing up."\
.format(busts[i-1],busts[i-1]/n))
        else:
            print("The dealer had {0} busted hands with a player win \
percentage of ({1:0.1%}) when {2} was facing up."\
.format(busts[i-1], busts[i-1]/n, i))

if __name__ == '__main__': main()
