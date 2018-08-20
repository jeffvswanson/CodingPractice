# cubeProperties.py
# A program to calculate the volume and surface area of a cube.
"""Same as Chapter 10 Programming Exercise 9, but for a cube. The constructor
should accept the length of a side as a parameter."""

from cubeClass import Cube

def main():
    
    edge = 0
    while edge <= 0:
        try:
            edge = float(input("Please enter the edge length of the cube: "))
            if radius <= 0:
                print("You have to enter a number greater than zero.")
        except(SyntaxError, NameError, TypeError, ValueError):
            print("You have to enter a number greater than zero.")
            continue

    cube = Cube(edge)

    volume = cube.volume()

    surfaceArea = cube.surfaceArea()

    if volume == 1:
        print("\nThe volume of the cube is {0:.2f} unit.".format(volume))
    else:
        print("\nThe volume of the cube is: {0:.2f} units.".format(volume))
    if surfaceArea == 1:
        print("\nThe surface area of the cube is: {0:.2f} unit."
    .format(surfaceArea))
    else:
        print("\nThe surface area of the cube is: {0:.2f} units."
    .format(surfaceArea))

main()
