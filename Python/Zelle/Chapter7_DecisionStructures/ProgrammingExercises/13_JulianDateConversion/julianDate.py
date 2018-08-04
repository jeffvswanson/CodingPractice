# julianDate.py
# A program that accepts the date in the form month/day/year and outputs
# the number of the day 1 through 366.
"""The days of the year are often numbered from 1 through 365 (or 366). This 
number can be computed in three steps using arithmetic:
(a) dayNum = 31(month - 1) + day
(b) if the month is after February subtract (4(month) + 23)//10
(c) if it's a leap year and after February 29, add 1

Write a program that accepts a date as month/day/year, verifies that it is a
valid date (see previous problem), and then calculates the corresponding day
number."""

def leapCheck(year):

    standardLeap = year % 4
    centuryLeap = year % 400
    centuryCheck = year % 100

    if centuryLeap == 0:
        leapYear = True
    elif standardLeap == 0 and centuryLeap != 0:
        if standardLeap == 0 and centuryCheck == 0:
            leapYear = False
        elif standardLeap == 0:
            leapYear = True
    else:
        leapYear = False

    return leapYear

def inputCheck(day, month, year):

    if month > 12 or month < 1:
        message = "Please enter a month between 1 and 12."
    elif day > 31 or day < 1:
        message = "Please enter a date between 2 and 31."
    elif year < 1:
        message = "Please enter a year greater than or equal to 1."
    else:
        message = True

    return message

def julianDate(day, month, year, leapYear):

    if month > 2 and leapYear == True:
        dayNum = 31 * (month - 1) + day - (4 * month + 23) // 10 + 1
    elif month > 2:
        dayNum = 31 * (month - 1) + day - (4 * month + 23) // 10
    else:
        dayNum = 31 * (month - 1) + day

    return dayNum

def main():

    print("This program checks if a date is valid.")
    try:
        month = int(input("Please enter the month in a number form: "))
        day = int(input("Please enter the day: "))
        year = int(input("Please enter the year: "))

        leapYear = leapCheck(year)

        message = inputCheck(day, month, year)

        if message != True:
            print(message)
        else:
            date = julianDate(day, month, year, leapYear)
            print("The Julian date is {0} for {1}/{2}/{3}.".format(date, \
            month, day, year))    
    except (ValueError, SyntaxError):
       print("You have to enter whole numbers. Exiting.")
main()
