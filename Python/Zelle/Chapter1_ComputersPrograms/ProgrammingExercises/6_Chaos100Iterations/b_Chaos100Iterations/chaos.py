# File: chaos.py
# A simple program illustating chaotic behavior.
"""The calculation performed in the chaos program from section 1.6 can be
written in a number of ways that are algebraically equivalent. Write a version
of the program for each of the following ways of doing the computation. Have
your modified programs print out 100 iterations of the calculation and compare
the results when run on the same input.

a) 3.9 * x * (1 - x)
b) 3.9 * (x - x * x)
c) 3.9 * x - 3.9 * x * x"""

def main():
    print("This program illustates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(100):
        x = 3.9 * (x - x * x)
        print(x)

main()
