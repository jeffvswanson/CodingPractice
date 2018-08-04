# convert.py
# A program to convert Celsius temps to Fahrenheit
"""Modify the convert.py program (Section 2.2) so that it computes and prints a
table of Celsius temperatures and the Fahrenheit equivalents every 10 degrees
from zero degrees Celsius to 100 degrees Celsius."""

def main():
    print("This program converts Celsius temperatures into Fahrenheit")
    print("degrees Celsius|\t|degrees Fahrenheit")
    print("-------------------------------------------")
    for celsius in range (0, 101, 10):
        fahrenheit = 9/5 * celsius + 32.0
        print("{0:0.1f} \tCelsius \t{1:0.1f} \tFahrenheit" \
              .format(celsius, fahrenheit))

main()
