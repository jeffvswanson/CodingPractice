# ladderLength.py
# A program to calculate the length of a ladder needed
# to get to a specific height on a house.
""" Write a program to determine the length of a ladder required to reach a
given height when leaned against a house. The height and angle of the ladder
are given as inputs. To compute length use:

length = height/sin(angle)
NOTE: The angle must be in radians. Prompt for an angle in degrees and use this
formula to convert:

radians = (pi / 180) * degrees"""

import math

def main():

    print("This program calculates the length needed for a ladder to reach a certain spot on a house.")
    print()
    height = float(input("Please enter the height you need to reach on the house in feet: "))
    degrees = float(input("Please enter the approximate angle the ladder will be from the ground in degrees: "))

    radians = degrees * math.pi / 180 # convert the degrees to radians
    length = height / math.sin(radians) # ladder height in feet

    print("You will need a ladder at least {:.1f} feet tall.".format(length))

main()
