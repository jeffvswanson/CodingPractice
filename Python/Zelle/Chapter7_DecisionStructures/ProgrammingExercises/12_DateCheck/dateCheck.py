# dateCheck.py
# A program that accepts the date in the form month/day/year and outputs
# whether or not the date is valid.
"""Write a program that accepts a date in the form month/day/year and outputs
whether or not the date is valid. For example, 5/24/1962 is valid, but 
9/31/2000. (September has only 30 days.)"""

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

def formatDate(day, month, year, leapYear):

    if month == 2 and day > 29:
        date = "February cannot have more than 29 days!"
    elif month == 2 and day == 29 and leapYear == True:
        date = "{0}/{1}/{2}".format(month, day, year)
    elif (month == 4 or month == 6 or month == 9 or month == 11) and day >= 31:
        date = "This month has less than 31 days."
    else:
        date = "{0}/{1}/{2}".format(month, day, year)

    return date

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
            date = formatDate(day, month, year, leapYear)
            print(date)    
    except (ValueError, SyntaxError): 
       print("You have to enter whole numbers. Exiting.")
main()
