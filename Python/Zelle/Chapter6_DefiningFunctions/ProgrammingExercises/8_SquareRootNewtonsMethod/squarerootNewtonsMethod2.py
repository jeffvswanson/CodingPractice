# squarerootNewtonsMethod2.py
# A program that attempts to find the square root of a number selected by the
# user by iterating Newton's method over a number of times selected by the user. The program then checks for accuracy.
"""Solve Programming Exercise 17 from Chapter 3 using a function
nextGuess(guess, x) that returns the next guess."""

import math

def nextGuess(guess, x):
    guess = (guess + x/guess) / 2
    return guess

def main():

    print("This program attempts to find the square root of a number selected\
 by the user using Newton's method and iterating a number of times selected\
 by the user. The program then checks for accuracy.")
    print()
    
    x = float(input("Please select the number of which you wish to find\
 the square root: "))
    n = int(input("Please select the number of times you wish to iterate\
 Newton's method: "))
    guess = x/2 # initialize the value of guess

    nextGuess(guess, x)
    
    for i in range(n):
        guess = nextGuess(guess, x)

    difference = math.sqrt(x) - guess
    print("The approximate square root is {0} and the difference\
 is {1} between the approximation and math.sqrt(x).".format(guess, difference))

main()
