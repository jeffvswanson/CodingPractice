# gcd.py
# A program that finds the greatest common divisor of two values using 
# Euclid's algorithm.
"""The greatest common divisor (GCD) of two values can be computed using 
Euclid's algorithm. Starting with the values m and n, we repeatedly apply the 
formula: n, m = m, n%m until m is 0. At that point, n is the GCD of the 
original m and n. Write a program that finds the GCD of two numbers using
this algorithm."""

def getInput():
    while True:
        try:
            m = int(input("Please enter first number you would like to find \
the GCD for seperated by a comma: "))
        except (SyntaxError, NameError, TypeError, ValueError):
            print("You have to enter a whole number zero or greater.")
            continue
        if m >= 0:
            break
    
    while True:
        try:
            n = int(input("Please enter the second number you would like to \
find the GCD for seperated by a comma: "))
        except (SyntaxError, NameError, TypeError, ValueError):
            print("You have to enter a whole number zero or greater.")
            continue
        if n >= 0:
            break
    
    return m, n

def main():

    print("This program find the greatest common divisor (GCD) of two values \
using Euclid's algorithm.")

    m, n = getInput()
    m0, n0 = m, n
    
    if m == 0:
        print("\nThe GCD of ({0}, {1}) = {1}.".format(m, n))
    elif n == 0:
        print("\nThe GCD of ({0}, {1}) = {0}.".format(n, m))
    else:
        while m != 0:
            n, m = m, n % m
        print("\nThe GCD of ({0}, {1}) = {2}.".format(m0, n0, n))			

main()
