# coffeeOrderCost.py
# A program to calculate the cost to order coffee.
"""The Konditorei coffee shop sells coffee at $10.50 a pound plus the cost of
shipping. Each order shigs for $0.86 per pound + $1.50 fixed cost for overhead.
Write a program that calculates the cost of an order."""

import math

def main():

    coffee = 10.50 # cost of coffee per pound
    pounds = 0 # pounds of coffee
    fixed = 1.50 # dollars, fixed overhead of shipping coffee
    shippingcost = 0.86 # dollars

    print("This program calculates the total cost to order and ship coffee.")
    print()
    
    pounds = float(input("Please input the total amount in pounds of coffee ordered: "))
    
    shipping = (coffee + shippingcost) * pounds + fixed

    print("The total cost with shipping is ${:.2f} dollars.".format(shipping))
    
main()
