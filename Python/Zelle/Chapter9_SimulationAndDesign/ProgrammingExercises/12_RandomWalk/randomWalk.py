# randomWalk.py
# A program to calculate how many steps away from a starting point you will end
# at assuming each step has a 50% chance to step forward or back.
"""A random walk is a particular kind of probabilistic simulation that models
certain statistical systems such as the Brownian motion of molecules. You can
think of a one-dimensional random walk in terms of coin flipping. Suppose you
are standing on a very long straight sidewalk that extends both in front of and
behind you. You flip a coin. If it comes up heads, you take a step forward; 
tails means to take a step backward.
    Suppose you take a random walk of n steps. On average, how many steps away 
from the starting point will you end up? Write a program to help you 
investigate this question."""

from random import random

def main():
    printIntro()
    n = getInput()
    walk = simWalk(n)
    printSummary(n, walk)

def printIntro():
    print("This program simulates a random walk along a straight line. You \
have a 50% chance of stepping forward or backward. The user chooses how many \
steps to take. After simulating the walk the program prints the number of \
steps away from the starting point the user would be.")

def getInput():
    #  Get the number of steps the user wants to take.
    n = 0
    while n < 1:
        try:
            n = int(input("Please enter the number of steps you want to take \
on your random walk: "))
        except (SyntaxError, NameError, TypeError, ValueError):
            print("You have to enter a whole number.")
            continue
        if n < 1:
            print("You have to simulate at least one coin flip.")
            continue
    return n

def simWalk(n):
    walk = 0
    for i in range(n):
        step = random()
        if step >= 0.5:
            walk = walk + 1
        else:
            walk = walk - 1

    return walk

def printSummary(n, walk):
    if walk == 0:
        print("After taking {0} random steps, you are exactly where you \
started.".format(n))
    elif walk > 0:
        print("After taking {0} random steps, you are {1} steps forward from \
where you started.".format(n, walk))
    else:
        # Convert walk to a positive number for printing
        walk = walk * -1
        print("After taking {0} random steps, you are {1} steps backward from \
where you started.".format(n, walk))

if __name__ == '__main__': main()
