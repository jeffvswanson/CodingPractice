# monteCarloPiEstimate.py
# Estimate pi using Monte Carlo analysis.
"""Monte Carlo techniques can be used to estimate the value of pi. Suppose you
have a round dartboard that just fits inside of a square cabinet. If you throw
darts randomly, the proportion that hit the dartboard vs. those that hit the 
cabinet (in the corners not covered by the board) will be determined by the
relative area of the dartboard and the cabinet. If n is the total number of 
darts randomly thrown (that land within the confines of the cabinet), and h is
the number that hit the board, it is easy to show that pi = 4(h/n).
    Write a program that accepts the "number of darts" as an input and then 
performs a simulation to estimate pi. Hint: You can use 2*random() - 1 to
generate the x and y coordinates of a random point inside a 2x2 square centered
at (0, 0). The point lies inside the inscribed circle if x^2 + y^2 <= 1."""

from random import random
import math

def main():

    printIntro()
    n = getInput()
    pi = sim(n)
    printSummary(n, pi)

def printIntro():
    print("This program estimates pi by simulating randomly throwing darts at \
a dart board.")

def getInput():
    n = 0
    while n < 1:
        try:
            n = int(input("Please enter the number of darts you want to throw \
the dart board: "))
        except (SyntaxError, NameError, TypeError, ValueError):
            print("You have to enter a whole number.")
            continue
        if n < 1:
            print("You have to simulate at least one dart throw.")
            continue
    return n

def sim(n):

    hit = 0
    for i in range(n):
        # dartLoc is the dart location to generate x and y  coordinates of a
        # random point inside a 2x2 square centered at (0,0). The point lies
        # inside the inscribed circle if x^2 + y^2 <= 1.
        dartLocX = 2 * random() - 1
        dartLocY = 2 * random() - 1
        
        if (dartLocX <= math.sqrt(1 - dartLocY ** 2)) \
        and (dartLocY <= math.sqrt(1 - dartLocX ** 2)):
            hit = hit + 1
        
    pi = 4 * (hit / n)

    return pi

def printSummary(n, pi):

    print("After throwing {0} simulated darts at the board, pi is \
approximately {1:0.2f}.".format(n, pi))

if __name__ == '__main__': main()
