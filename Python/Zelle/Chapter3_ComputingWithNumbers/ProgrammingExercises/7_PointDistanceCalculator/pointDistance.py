# pointDistance.py
# A program which calculates the distance between two points
# on a Cartesian plane.
"""Write a program that accepts two points (see previous problem) and
determines the distance between them.

disance = sqrt((x2-x1)^2+(y2-y1)^2)"""

import math

def main():

    print("This program calculates the distance between two points on a Cartesian plane.")

    x1= float(input("Please enter the first x coordinate, x1: "))
    y1 = float(input("Please enter the first y coordinate, y1: "))
    print()
    x2= float(input("Please enter the first x coordinate, x1: "))
    y2 = float(input("Please enter the first y coordinate, y1: "))

    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    print("The distance between the two points is {:.1f} units.".format(distance))

main()
