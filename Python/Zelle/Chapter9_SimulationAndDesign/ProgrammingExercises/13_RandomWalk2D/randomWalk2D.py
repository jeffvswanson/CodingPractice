# randomWalk2D.py
# A program to calculate how many steps away from a starting point you will end
# at assuming each step has a chance to step forward, back, left, or right.
"""Suppose you are doing a random walk (see CH9 Programming Exercise 12) on the 
blocks of a city street. At each "step" you choose to walk one block (at 
random) either forward, backward, left or right. In n steps, how far do you 
expect to be from your starting point? Write a program to help answer this
question."""

from random import random

def main():
    printIntro()
    n = getInput()
    # walk is forward/backward steps from origin
    # lat represents left/right steps from origin
    walk, lat = simWalk(n)
    printSummary(n, walk, lat)

def printIntro():
    print("This program simulates a random walk. You have a chance of stepping \
forward, backward, left, or right. The user chooses how many steps to take. \
After simulating the walk the program prints the numbe of steps away from the \
starting point the user would be.")

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
            print("You have to simulate at least one step.")
            continue
    return n

def simWalk(n):
    # set the forward and back walk variable and left and right lat variable.
    walk = 0
    lat = 0
    for i in range(n):
        step = random()
        if step < 0.25:
            walk = walk + 1
        elif step >= 0.25 and step < 0.5:
            walk = walk - 1
        elif step >= 0.5 and step < 0.75:
            lat = lat + 1
        else:
            lat = lat - 1
    return walk, lat

def printSummary(n, walk, lat):
    if walk == 0 and lat == 0:
        print("After taking {0} random steps, you are exactly where you \
started.".format(n))
    elif walk > 0 and lat > 0:
        print("After taking {0} random steps, you are {1} steps forward and \
{2} steps right from where you started.".format(n, walk, lat))
    elif walk > 0 and lat < 0:
        # Convert lat to a positive number for printing
        lat = lat * -1
        print("After taking {0} random steps, you are {1} steps forward and \
{2} steps left from where you started.".format(n, walk, lat))
    elif walk < 0 and lat > 0:
        # Convert walk to a positive number for printing
        walk = walk * -1
        print("After taking {0} random steps, you are {1} steps backward and \
{2} steps right from where you started.".format(n, walk, lat))
    else:
        # Convert walk and lat to a positive number for printing
        lat = lat * -1
        walk = walk * -1
        print("After taking {0} random steps, you are {1} steps backward and \
{2} steps left from where you started.".format(n, walk, lat))

if __name__ == '__main__': main()
