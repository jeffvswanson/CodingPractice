# isItPrime.py
# A program that determines if a user input number is prime.
"""A positive whole number n > 2 is prime if no number between 2 and sqrt(n) 
(inclusive) evenly divides n. Write a program that accepts a value of n as 
input and determines if the value is prime. If n is not prime, your program
should quit as soon as it finds a value that evenly divides n."""

import math

def getN():
    try:
        while True:
            n = int(input("Please enter a whole number greater than two you \
would want to check as prime: "))
            if n > 2:
                break
    except (SyntaxError, NameError, TypeError, ValueError) as err:
        print("You have to enter a whole number greater than two. Exiting.")
        print(err.args)
        quit(0)
    return n

def primeCheck(n):
    x = 2
    prime = False        
    while x <= math.sqrt(n):
        if n % x == 0:
            prime = True
            break
        else: 
            x += 1
    return x, prime

def main():

    print("A positive whole number n > 2 is prime if no number between 2 and \
the square root of n evenly divides n. This program determines if a number is \
prime.")

    n = getN()

    x, prime = primeCheck(n)

    if prime == True:
        print("The number {0} is not prime and divisible by {1}.".format(n, x))
    else:
        print("The number {0} is prime.".format(n))        
main()
