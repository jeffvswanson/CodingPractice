# findThePrimes.py
# A program that finds all the primes less than or equal to n.
"""Modify the previous program to find every prime number less than or equal to
n."""

import math

def getN():
    
    while True:
        try:
            n = int(input("Please enter a whole number greater than one you \
would want to check as prime: "))
        except (SyntaxError, NameError, TypeError, ValueError):
            print("You have to enter a whole number greater than one.")
            continue
        if n > 1:
            break
    return n

def checkPrimes(n):

    divisible = []
    # Initialize the checklist
    checklist = [1, 2]

    # Add numbers to the checklist, but not even ones.
    for i in range(3, n+1, 2):
        checklist.append(i)

    # Check the list for divisible elements and make a list with them.
    for j in checklist:
        x = 3 # Don't have to worry about 2 since it's already included.
        while x <= math.sqrt(j):
            if j % x == 0:
                divisible.append(j)
                break #break out of the decision and restart.
            else:
                x += 1

    # Remove the divisible elements from the list to be left with a list of 
    # primes alone.
    for k in divisible:
        checklist.remove(k)
        
    return checklist

def main():

    print("This program finds all the prime numbers between 1 and n.")

    n = getN()
    # Create the list of primes to print.
    primes = checkPrimes(n)

    print("The prime numbers between 1 and", n, "are", primes)
main()
