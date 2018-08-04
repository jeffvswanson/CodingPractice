# sphereproperties2.py
# A program to compute the volume and surface area of a sphere.
"""Write definitions for these functions:

sphereArea(radius) Returns the surface area of a sphere having a given radius.

sphereVolume(radius) Returns the volume of a sphere having the given radius.

Use your functions to solve Programming Exercise 1 from Chapter 3."""

import math

def sphereArea(radius):
    area = 4 * math.pi * radius ** 2
    return area

def sphereVolume(radius):
    volume = (4/3) * math.pi * radius ** 3
    return volume

def main():

    print("Calculate a spheres surface area and volume.")
    volume = 0
    area = 0
    radius = 0
    radius = float(input("Please enter the radius of the sphere: "))

    area = sphereArea(radius)

    volume = sphereVolume(radius)
    
    print("\nThe volume of the sphere is: {0:0.2f}".format(volume))

    print("\nThe surface area of the sphere is: {0:0.2f}".format(area))

main()
