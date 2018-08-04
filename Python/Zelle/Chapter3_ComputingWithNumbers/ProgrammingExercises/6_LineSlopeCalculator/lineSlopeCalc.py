# lineSlopeCalc.py
# A program tath calculates the slope between two points on a line.
"""Two points in a plane are specified using the coordinates (x1,y1) and
(x2, y2). Write a program that calculates the slope of a line through two
(non-vertical) points entered by the user.

    slope = (y2-y1)/(x2-x1)"""

import math

def main():

    print("This program calculates the slope of a line between two points.")

    x1= float(input("Please enter the first x coordinate, x1: "))
    y1 = float(input("Please enter the first y coordinate, y1: "))
    print()
    x2= float(input("Please enter the first x coordinate, x1: "))
    y2 = float(input("Please enter the first y coordinate, y1: "))
    slope = (y2 - y1)/(x2 - x1)

    print("The slope of the line, m, is {:0.1f}.".format(slope))

main()
