# convertPoundsToKilograms.py
# A program to convert pounds to kilograms.
# Assumes gravity is 9.8 m/s^2
"""Write a program to perform a unit conversion of your choosing. Make sure that
the program prints an introduction that explains what it does."""

def main():
    print("This program converts pounds to kilograms.")
    pound = eval(input("How many pounds do you want to convert? "))
    kilo = pound/2.204
    print("The mass is {0:0.1f} kilograms.".format(kilo))

main()
