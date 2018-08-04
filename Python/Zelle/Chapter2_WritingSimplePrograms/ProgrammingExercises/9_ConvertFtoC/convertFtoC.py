# convertFtoC.py
# A program to convert Celsius temps to Fahrenheit
"""Write a program that converts temperatures fro Fahrenheit to Celsius."""

def main():
    print("This program converts Fahrenheit temperatures into Celsius")
    fahrenheit = eval(input("What is the temperature in Fahrenheit? "))
    celsius = (fahrenheit - 32) / (9/5)
    print("The temperature is {0:0.1f} degrees Celsius.".format(celsius))

main()
