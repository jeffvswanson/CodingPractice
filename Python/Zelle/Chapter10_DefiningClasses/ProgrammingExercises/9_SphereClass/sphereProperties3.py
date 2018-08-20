# sphereProperties3.py
# A program to calculate the surface area and volume of a sphere.
"""Write a class to represent spheres. Your class should implement the 
following methods:
__init__(self, radius) Creates a sphere having the given radius.
getRadius(self) Returns the radius of this sphere.
surfaceArea(self) Returns the surface area of the sphere.
volume(self) Returns the volume of the sphere.

Use your new class to solve Programming Exercise 1 from Chapter 3"""

from sphereClass import Sphere

def main():

    radius = 0
    while radius <= 0:
        try:
            radius = float(input("Please enter the radius of the sphere: "))
            if radius <= 0:
                print("You have to enter a number greater than zero.")
        except(SyntaxError, NameError, TypeError, ValueError):
            print("You have to enter a number greater than zero.")
            continue

    sphere = Sphere(radius)

    volume = sphere.volume()

    surfaceArea = sphere.surfaceArea()

    print("\nThe volume of the sphere is {0:.2f} units.".format(volume))
    print("\nThe surface area of the sphere is {0:.2f} units."
    .format(surfaceArea))

main()
