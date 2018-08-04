# sumAndSumOfCubes.py
# A program that sums the first n natural numbers
# and the sum of the cubes of the first n natural numbers
"""Write definitions for the following two functions:

sumN(n) returns the sum of the first n natural numbers.

sumNCubes(n) returns the sum of the cubes of the first n natural numbers.

Then use the functions in a program that prompts a user for an n and prints out
the sum of the first n natural numbers and the sum of the cubes of the first n
natural numbers."""

def sumN(n):
    summed = 0
    for i in range(n+1):
        summed = summed + i
    return summed

def sumNCubes(n):
    cubed = 0
    for i in range(n+1):
        cubed = cubed + i ** 3
    return cubed

def main():

    print("Calculate the sum of the first n natural number \
and the sum of the cubes of the first n natural numbers")

    n = int(input("Please enter how many numbers you want to sum and cube: "))

    summed = sumN(n)

    cubed = sumNCubes(n)

    print("The sum of n natural numbers is {0}.\n".format(summed))
    print("The sum of the cubes of n natural numbers is {0}.".format(cubed))

main()
