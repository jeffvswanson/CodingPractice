# babysitterWageCalc.py
# A program that accepts a starting time and ending time in hours and minutes
# to calculate the total babysitting bill. The start and end times are in a
# single 24 hour period. Partial hours are prorated.
"""A babysitter charges $2.50 an hour until 9:00 PM when the rate drops to
$1.75 an hour (the children are in bed). Write a program that accepts a
starting time and ending time in hours and minutes and calculates the total
babysitting bill. You may assume that the starting and ending times are in a
single 24-hour period. Partial hours should be prorated."""

from datetime import datetime

def getTimes():
    start = input("What time did the babysitter start (HH:MM)? ")
    end = input("\nWhat time did you come home (HH:MM)? ")

    return start, end

def calcWage(start, end):
    lowWage = 1.75
    highWage = 2.50
    startHour = int(start[:2])
    startMin = int(start[3:])/60
    endHour = int(end[:2])
    endMin = int(end[3:])/60

    # Get the time after 9 PM and before 12 AM
    if endHour > 9:
        lowWageTime = (endHour + endMin) - 9
    else:
        lowWageTime = 0

    # Calculate time worked before 9 PM.
    if startHour < 9:
        highWageTime = 9 - (startHour + startMin)
    else:
        highWageTime = 0

    pay = (highWageTime * highWage) + (lowWageTime * lowWage)
    
    return pay


def main():
    # Introduction
    print("""This program accepts the number of hours and minutes a babysitter
worked and calculates how much is owed. Prevailing wage is $2.50, after 9 p.m.
the wage goes to $1.75. Partial hours are prorated. The babysitter goes home
at 12AM.""")
    try:
    # Get the start and end times.
    # Assume single 24-hour period means before 12 AM.
        start, end = getTimes()

        pay = calcWage(start, end)

        print("You owe the babysitter ${0:0.2f}.".format(pay))
    except (ValueError, SyntaxError):
        print("You need ti input time in numbers as HH:MM. Exiting.")

main()
