# volleyballRallyScoring.py
# A program that simulates a volleyball game with rally scoring
"""Most sanctioned volleyball is now played using rally scoring. In this 
system, the team that wins a rally is awarded a point, even if they are
not the serving team. Games are played to a score of 25. Design and 
implement a simulation of volleyball using rally scoring."""

from random import random

def main():
	
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB, n)

def printIntro():
	
    print("This program simulates a game of volleyball between two \
teams called 'A' and 'B'. The abilities of each team is indicated by a \
probability (a number betweeen 0 and 1) that the team wins the point when \
serving. Team A always has the first serve.")

def getInputs():
	# Returns the three simulation parameters.
    a = b = 0
    while a + b != 1:
        print("Team A and Team B probability of winning added together \
must equal 1.")
        while True:
            try:
                a = float(input("What is the probability Team A \
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
                b = float(input("What is the probability Team B \
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
# Simulates n games of volleyball between team whose
# 	abilities are represented by the probability of winning a serve.
# Returns number of wins for A and B

    winsA = winsB = 0

    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simOneGame(probA, probB):
    # Simulates a single game of volleyball between teams whose
    # 	abilities are represented by the probability of winning a serve.
    # Returns final scores for teams A and B

    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if random() < probA:
            scoreA = scoreA + 1
        else:
            scoreB = scoreB + 1
                    
    return scoreA, scoreB

def gameOver(a, b):
    # a and b represent scores for a volleyball game
    # Returns True if the game is over, otherwise False.

    return a == 25 or b == 25
	
def printSummary(winsA, winsB, n):
    # Prints a summary of wins for each team

    print("\nGames simulated:", n)
    print("Wins for team A: {0} ({1:0.1%})".format(winsA, winsA/n))
    print("Wins for team B: {0} ({1:0.1%})".format(winsB, winsB/n))
	
if __name__ == '__main__': main()
