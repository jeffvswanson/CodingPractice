# rballShutout.py
# A program that calculates who will win racquetball matches and reports
# the number of wins per player, percentage of wins, number of shutouts,
# and the percentage of wins that are shutouts.
"""Revise the racquetball simulation to take shutouts into account. Your 
updated version should report for both players the number of wins, percentage
wins, number of shutouts, and percentage of wins that are shutouts."""

from random import random

def main():
    
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB, shutoutsA, shutoutsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB, shutoutsA, shutoutsB, n)

def printIntro():
    
    print("This program simulates a game of racquetball between two \
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
                a = float(input("What is the probability player A \
                wins a serve? "))
            except (SyntaxError, NameError, TypeError, ValueError):
                print("You have to enter a decimal between 0 and 1.")
                continue
            if a > 1 or a < 0:
                print("You have to enter a decimal between 0 and 1.")
                continue
            else: break

        while True:
            try:
                b = float(input("What is the probability player B \
                wins a serve? "))
            except (SyntaxError, NameError, TypeError, ValueError):
                print("You have to enter a decimal between 0 and 1.")
                continue
            if a > 1 or a < 0:
                print("You have to enter a decimal between 0 and 1.")
                continue
            else: break

    n = 0
    while n < 1:
        try:
            n = int(input("How many games to simulate? "))
        except (SyntaxError, NameError, TypeError, ValueError):
            print("You have to enter a whole number.")
            continue
        if n < 1:
            print("You have to simulate at least one game.")
            continue

    return a, b, n

def simNGames(n, probA, probB):
    # Simulates n games of racquetball between players whos
    # 	abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B

    winsA = winsB = 0
    shutoutsA = shutoutsB = 0

    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
            if scoreB == 0:
                shutoutsA = shutoutsA + 1
        else:
            winsB = winsB + 1
            if scoreA == 0:
                shutoutsB = shutoutsB + 1
    return winsA, winsB, shutoutsA, shutoutsB

def simOneGame(probA, probB):
    # Simulates a single game of racquetball between players whose
    # 	abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B

    serving = "A"
    scoreA = 0
    scoreB = 0
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
    # a and b represent scores for a racquetball game
    # Returns True if the game is over, otherwise False.

    return a == 15 or b == 15
    
def printSummary(winsA, winsB, shutoutsA, shutoutsB, n):
    # Prints a summary of wins for each player

    print("\nGames simulated:", n)
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n))
    if winsA != 0:
        print("Shutouts for A: {0} ({1:0.1%})"\
        .format(shutoutsA, shutoutsA/winsA))
    else: 
        print("A cannot have any shutouts.")
    print("\nWins for B: {0} ({1:0.1%})".format(winsB, winsB/n))
    if winsB != 0:
        print("Shutouts for B: {0} ({1:0.1%})"\
        .format(shutoutsB, shutoutsB/winsB))
    else:
        print("B cannot have any shutouts.")
    

if __name__ == '__main__': main()
