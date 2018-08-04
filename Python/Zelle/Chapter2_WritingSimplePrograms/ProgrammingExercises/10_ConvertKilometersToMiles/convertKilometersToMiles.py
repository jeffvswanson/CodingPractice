# convertKilometersToMiles.py
# A program to convert kilometers to miles
"""Write a program that converts distances measured in kilometers to miles. One
kilometer is approximately 0.62 miles."""

def main():
    print("This program converts kilometers to miles.")
    km = eval(input("What is the distance in kilometers? "))
    miles = 0.62 * km
    print("The distance is {0:0.1f} miles.".format(miles))

main()
