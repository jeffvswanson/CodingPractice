# pizzaCostPerSquareInch.py
# A program that calculates the cost per square inch of pizza.
"""Write a program that clculates the cost per square inch of a circular pizza,
given its diameter and price. The formula for area is A = pi * r^2."""

import math

def main():

    area = 0
    radius = 0
    price = 0
    cost = 0

    print("This program calculates the cost of pizza per square inch.")

    radius = float(input("Please enter the radius of the pizza in inches: "))
    price = float(input("Please enter the price of the pizza: "))

    area = math.pi * radius ** 2
    cost = price / area

    print("The cost per square inch of the pizza is ${0:.4f} per square inch.".format(cost))

main()
