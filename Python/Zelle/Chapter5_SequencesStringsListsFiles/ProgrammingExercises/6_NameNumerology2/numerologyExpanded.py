# numerologyExpanded.py
# A program designed to calculate the numeric value of a full name provided
# as input.
"""Expand your solution from 5 to allow the calculation of a complete name such
as "John Marvin Zelle" or "John Jacob Jingleheimer Smith." The total value is
just the sum of the numeric values of all the names."""

def main():

    print("This program accepts a single name and then returns the numeric \
value of the name.")

    # a = 1, b = 2, ..., z = 26.
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letters = list(alphabet)

    # Get the name to calculate and make it a list.
    name = input("Please enter a name: ")
    name = name.lower()
    name = name.split()
    namelist = list(name)
    namelist = "".join(namelist)

    numerology = 0

    # Loop through the list to add the values of the letters together
    for f in namelist:

        numerology = numerology + letters.index(f)+1

    print("\nThe numeric value of the name is {0}.".format(numerology))

main()
