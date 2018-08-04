# calcLeapYear.py
# A program that checks if a year is a leap year.
"""A year is a leap year if it is divisible by 4, unless it is a century that 
is not divisible by 400. (1800 and 1900 are not leap years while 1600 and 2000)
are.) Write a program that calculates whether a year is a leap year."""

def leapCheck(year):

    standardLeap = year % 4
    centuryLeap = year % 400
    centuryCheck = year % 100

    if centuryLeap == 0:
        message = "{0} is a leap year!".format(year)
    elif standardLeap == 0 and centuryLeap != 0:
        if standardLeap == 0 and centuryCheck == 0:
            message = "{0} is not a leap year.".format(year)
        elif standardLeap == 0:
            message = "{0} is a leap year!".format(year)
    else:
        message = "{0} is not a leap year.".format(year)

    return message

def main():
    print("This program checks if a year is a leap year.")
    try:
        year = int(input("Please enter the year you wish to check: "))

        message = leapCheck(year)

        print(message)
    except (ValueError, SyntaxError):
        print("You need to enter a whole number for the year. Exiting.")
    
main()
