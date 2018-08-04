# easterCalculator2.py
# A program that calculates the date of Easter between the years 1900-2099.
"""The formula for Easter in Programming Exercise 7.09 works for every year in 
the range 1900-2099 except for 1954, 1981 2049, and 2076. For these 4 years it
produces a date that is one week too late. Modify the program to work for the 
entire range 1900-2099."""

def calcEaster(year):
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7

    date = 22 + d + e

    if year == 1954 or year == 1981 or year == 2049 or year == 2076:
        date = date - 7
    
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
1900-2099.")
        year = int(input("Please enter the year you would like to know the \
date of Easter: "))
        
        if year > 2099 or year < 1900:
            print("You can only put in a date between 1900 and 2099.")
        else:
            easterDay, month = calcEaster(year)
            print("Easter in {0} is on {1} {2}".format(year, easterDay, month))
    except (ValueError, SyntaxError):
        print("You must enter the year as a whole number. Exiting.")
main()
