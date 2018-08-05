# goldbachConjecture.py
# A program that gets a number from the user, checks to make sure it is even, and then finds two prime 
# numbers that sum to the number.
"""The Goldbach conjecture asserts that every number is the sum of two prime
numbers. Write a program that gets a number from the user, checks to make 
sure that it is even, and then finds two prime numbers that add up to the
number."""

import math

def getN():
    while True:
        try:
            n = int(input("Please enter the even number you would like to \
check: "))
        except (SyntaxError, NameError, TypeError, ValueError):
            print("You have to enter an even number greater than zero.")
            continue
        if n % 2 != 0:
            print("You have to enter an even number greater than zero")
            continue
        else:
            break
    return n       

def checkPrimes(n):

    divisible = []
    # Initialize the checklist
    checklist = [1, 2]

    # Since all even numbers are divisible by 2 make a list without them.
    for i in range(3, n, 2):
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

def findPrimes(primes, n):
    p1, p2 = 0, 0
    while primes[p1] + primes[p2] != n:
        if p2 <= p1:
            p2 += 1
        else:
            p2 = 0
            p1 += 1
    
    p1 = primes[p1]
    p2 = primes[p2]

    return p1, p2

def main():

    print("The Goldbach conjecture asserts that every even number is the sum \
of two prime numbers.")
    # Get the even number from the user
    n = getN()

    primes = checkPrimes(n)
   
    p1, p2 = findPrimes(primes, n)

    print(p1, "+", p2, "=", n)	

main()
