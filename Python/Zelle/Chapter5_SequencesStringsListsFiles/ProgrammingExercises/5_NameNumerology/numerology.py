# numerology.py
# A program designed to calculate the numeric value of a single name provided
# as input.
"""Numeroligists claim to be able to determine a person's character traits based
on the "numeric value" of a name. The value of a name is determined by summing
up the values of the letters of the name where "a" is 1, "b" is 2, "c" is 3, up
to "z" being 26. For example, the name "Zelle" would have the value:
26 + 5 + 12 + 12 + 5 = 60 (which happens to be a very auspicious number, by the
way). Write a program that calculates the numeric value of a single name
provided as input."""

def main():

    print("This program accepts a single name and then returns the numeric \
value of the name.")

    # a = 1, b = 2, ..., z = 26.
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letters = list(alphabet)

    name = input("Please enter a single name: ")
    name = name.lower()
    namelist = list(name)

    numerology = 0

    for f in namelist:

        numerology = numerology + letters.index(f)+1

    print("\nThe numeric value of the name is {0}.".format(numerology))

main()
