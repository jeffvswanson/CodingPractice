# convert.py
# A program to convert Celsius temps to Fahrenheit
"""A user-friendly program should print an introduction that tells the user what
the program does. Modify the convert.py program (section 2.2) to print an
introduction."""

def main():
    print("This program converts Celsius temperatures into Fahrenheit")
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()
