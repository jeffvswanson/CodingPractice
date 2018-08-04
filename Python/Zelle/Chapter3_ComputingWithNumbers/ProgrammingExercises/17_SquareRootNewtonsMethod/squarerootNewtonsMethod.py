# squarerootNewtonsMethod.py
# A program that attempts to find the square root of a number selected by the
# user by iterating Newton's method over a number of times selected by the user. The program then checks for accuracy.
"""You have seen that the math library contains a function that computes the
square root of numbers. In this exercise, you are to write your own algorithm
for computing square roots. One way to solve this problem is to use a guess-and-
check approach. You first guess what the square root might be, ant then see how
close your guess is. You can use this information to make another guess and
continue guessing until you have found the square root (or a close approximation
to it). One particularly good way of making guesses is to use Newton's method.
Suppose x is the number we want the root of, and guess ir the current guessed
answer. The guess can be improved by computing the next guess as:
(guess + (x/guess))/2
Write a program that implements Newton's method. The program should prompt the
user for the value to find the square root of (x) and the number of times to
improve the guess. Starting with a guess value of x/2, your program should loop
the specified number of times applying Newton's method and report the final
value of guess. You should also subtract your estimate from the value of
math.sqrt(x) to show how close it is."""

import math

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
    
    for i in range(n):

        guess = (guess + x/guess) / 2

    difference = math.sqrt(x) - guess
    print("The approximate square root is {0} and the difference\
 is {1} between the approximation and math.sqrt(x).".format(guess, difference))

main()
