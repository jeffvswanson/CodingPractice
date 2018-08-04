# easterCalculator.py
# A program that calculates the date of Easter between the years 1982-2048.
"""A formula for computing Easter in the years 1982-2048, inclusive, is as 
follows: let a = year%19, b = year%4, c = year %7, d = (19a + 24)%30,
e = (2b + 4c + 6d +5)%7. The date of Easter is March 22 + d + e (which could be
in April). Wirte a program that inputs a year, verifies that it is in the
proper range, and then prints out the date of Easter that year."""

def calcEaster(year):
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7

    date = 22 + d + e

    if date <= 31:
        easterDay = date
        month = "March"
    else:
        easterDay = date - 31
        month = "April"

    return easterDay, month

def main():
    try:
        print("This program calculates the date of Easter between the years \
1982-2048.")
        year = int(input("Please enter the year you would like to know the \
date of Easter: "))
        
        if year > 2048 or year < 1982:
            print("You can only put in a date between 1982 and 2048.")
        else:
            easterDay, month = calcEaster(year)
            print("Easter in {0} is on {1} {2}".format(year, easterDay, month))
    except (ValueError, SyntaxError):
        print("You need to put in a whole number for the year. Exiting.")
main()
