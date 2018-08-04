# areaTriangle
# A program used to calculate the area of a triangle.
"""Write a program to calculate the area of a triangle given the length of its
three sides - a, b, and c - using these formulas:
s = (a + b + c)/2
A = sqrt(s(s - a)(s - b)(s - c))"""

import math

def main():

    print("This value calculates the area of a triangle provided the lengths of three sides are known.")
    print()
    a = float(input("Please enter the length of side a: "))
    b = float(input("Please enter the length of side b: "))
    c = float(input("Please enter the length of side c: "))

    s = (a + b + c)/2

    area = math.sqrt(s * (s-a)*(s-b)*(s-c))

    print("The area of the triangle is {:.2f} units.".format(area))
    
    
main()
