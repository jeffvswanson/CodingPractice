# fiveOfAKindDiceSimulator.py
# Simulates the probability of getting five of a kind in a single dice roll
"""Write a program that performs a simulation to estimate the probability of
rolling five of a kind in a single roll of five six-sided dice."""

from random import randrange

def main():
    printIntro()
    n = getInput()
    fiveOfAKind = simRolls(n)
    printSummary(n, fiveOfAKind)

def printIntro():
    print("This program estimates the likelihood of rolling a five of a kind \
on the first roll of a set of five die.")

def getInput():
    n = 0
    while n < 1:
        try:
            n = int(input("Please enter the number of dice rolls you want to \
simulate: "))
        except (SyntaxError, NameError, TypeError, ValueError):
            print("You have to enter a whole number.")
            continue
        if n < 1:
            print("You have to simulate at least one dice roll.")
            continue
    return n

def simRolls(n):
    fiveOfAKind = 0
    for i in range(n):
        # rollResult will return True (1) if five of a kind, else False (0)
        rollResult = simOneRoll()
        fiveOfAKind = fiveOfAKind + rollResult
    return fiveOfAKind

def simOneRoll():
    # Roll five die
    # Accumulate the dice roll in a list
    dice = []
    for i in range(5):
        dice.append(randrange(1,7))
    # Convert the list down to a set. If the set has length of 1 (all values
    # duplicate) then the roll is five of a kind.
    if len(set(dice)) == 1:
        return True
    else:
        return False

def printSummary(n, fiveOfAKind):
    print("After rolling the dice {0} times, the percentage of five of a \
kinds is approximately {1:0.4%} in one throw.".format(n, fiveOfAKind/n))

if __name__ == '__main__': main()