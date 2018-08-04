# sphereProperties.py
# A program to compute the volume and surface area of a sphere.
"""Write a program to calculate the volume and surface area of a sphere from its
radius, given as input. Here are some formulas that might be useful:

V = 4/3*pi * r^3
A = 4 * pi * r^2"""

import math

def main():

    print("Calculate a sphere's surface area and volume.")
    volume = 0
    area = 0
    radius = 0
    radius = float(input("Please enter the radius of the sphere: "))

    volume = (4/3) * math.pi * radius ** 3
    area = 4 * math.pi * radius ** 2

    print()
    print("The volume of the sphere is:", volume)
    print()
    print("The surface area of the sphere is:", area)

main()
