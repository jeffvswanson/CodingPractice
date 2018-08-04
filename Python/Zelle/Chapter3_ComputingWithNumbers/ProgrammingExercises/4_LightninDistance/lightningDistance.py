# lightningDistance.py
# A program to calculate the how far away lightning is based on observation.
"""Write a program that determines the distance to a lightning strike based on
the time elapsed between the flash and the sound of thunder. The speed of sound
is approximately 1100 ft/sec and 1 mile is 5280 feet."""

import math

def main():

    time = 0 # sec
    speedOfSound = 1100 # ft/sec
    mile = 5280 # feet

    print("This program is used to calculate how far lightning is from an observer.")
    print()

    time = int(input("Please enter the time in seconds from when you saw the lightning to hearing the thunder. "))
    distance = time * speedOfSound / mile # miles

    print()
    print("The lightning is {:0.1f} miles from the observer.".format(distance))

main()
