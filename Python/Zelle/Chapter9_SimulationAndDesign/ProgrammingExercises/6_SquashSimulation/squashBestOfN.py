# squashBestOfN.py
# A program that calculates who will win best of n squash matches.
"""Revise the squash simulation so that it computes the results for best 
of n game matches. First service alternates, so player A serves first in the 
odd games of the match, and player B serves first in the even games."""

from random import random

def main():
    
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB, n)

def printIntro():
    
    print("This program simulates a game of squash between two \
players called 'A' and 'B'. The abilities of each players is indicated by a \
probability (a number betweeen 0 and 1) that the player wins the point when \
serving. Player A always has the first serve.")

def getInputs():
    # Returns the three simulation parameters.
    a = b = 0
    while a + b != 1:
        print("Player A and Player B probability of winning added together \
must equal 1.")
        while True:
            try:
                a = float(input("What is the probability player A wins a \
serve? "))
            except (SyntaxError, NameError, TypeError, ValueError):
                print("You have to enter a decimal between 0 and 1.")
                continue
            if a > 1 or a < 0:
                print("You have to enter a decimal between 0 and 1.")
                continue
            else: break

        while True:
            try:
                b = float(input("What is the probability player B wins a \
serve? "))
            except (SyntaxError, NameError, TypeError, ValueError):
                print("You have to enter a decimal between 0 and 1.")
                continue
            if a > 1 or a < 0:
                print("You have to enter a decimal between 0 and 1.")
                continue
            else: break

    while True:
        try:
            n = int(input("How many games to simulate? "))
        except (SyntaxError, NameError, TypeError, ValueError):
            print("You have to enter a whole number.")
            continue
        if n < 1:
            print("You have to simulate at least one game.")
            continue
        else: break
            
    return a, b, n

def simNGames(n, probA, probB):
    # Simulates n games of squash between players whos
    # 	abilities are represented by the probability of winning a serve.
    # First service alternates, player A serve first odd games of the match
    #       player B serves first in the even games of the match.
    # Returns number of wins for A and B

    winsA = winsB = 0

    for i in range(1, n+1):
        while (winsA * 2 < (n+1)) and (winsB * 2 < (n+1)):
            scoreA, scoreB = simOneGame(probA, probB, i)
            if scoreA > scoreB:
                winsA = winsA + 1
            else:
                winsB = winsB + 1
    return winsA, winsB

def simOneGame(probA, probB, match):
    # Simulates a single game of squash between players whose
    # 	abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B

    scoreA = 0
    scoreB = 0
    if match % 2 != 0:
        serving = "A"
        while not gameOver(scoreA, scoreB):
            if serving == "A":
                if random() < probA:
                    scoreA = scoreA + 1
                else:
                    serving = "B"
            else:
                if random() < probB:
                    scoreB = scoreB + 1
                else:
                    serving = "A"
    else:
        serving = "B"
        while not gameOver(scoreA, scoreB):
            if serving == "A":
                if random() < probA:
                    scoreA = scoreA + 1
                else:
                    serving = "B"
            else:
                if random() < probB:
                    scoreB = scoreB + 1
                else:
                    serving = "A"
                    
    return scoreA, scoreB

def gameOver(a, b):
    # a and b represent scores for a squash game
    # Returns True if the game is over, otherwise False.
    if a >= 10 and a > b + 2:
        return True
    elif b >= 10 and b > a + 2:
        return True
    else:
        return False
    
def printSummary(winsA, winsB, n):
    # Prints who won the best of n matches

    if winsA > winsB:
            print("\nPlayer A won best", winsA, "of", n, "matches.")
    else:
            print("\nPlayer B won best", winsB, "of", n, "matches.")
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/(winsA + winsB)))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/(winsA + winsB)))

if __name__ == '__main__': main()