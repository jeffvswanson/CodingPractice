# pizzacostpersquareinch2.py
# A program that calculates the cost per square inch of pizza.
"""Redo Programming Exercise 2 from Chapter 3. Use two functions-one to compute
the area of a pizza, and one to compute the cost per square inch."""

import math

def pizzaArea(radius):
    area = math.pi * radius ** 2
    return area

def costPerSquareInch(price, area):
    cost = price / area
    return cost

def main():

    area = 0
    radius = 0
    price = 0
    cost = 0

    print("This program calculates the cost of pizza per square inch.")

    radius = float(input("Please enter the radius of the pizza in inches: "))

    price = float(input("Please enter the price of the pizza: "))

    area = pizzaArea(radius)

    cost = costPerSquareInch(price, area)
    print("The area of the pizza is {0:0.2f} square inches.".format(area))
    print("The cost per square inch of the pizza is ${0:0.2f} per square inch."\
          .format(cost))

main()
