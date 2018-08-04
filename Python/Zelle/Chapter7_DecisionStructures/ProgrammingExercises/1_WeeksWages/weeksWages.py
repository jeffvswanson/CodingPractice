# weeksWages.py
# A program that accepts the number of hours worked and the hourly rate 
# to calculate the total wages for the week
# Over 40 hours pays time-and-a-half in a given week.
"""Many companies pay time-and-a-half for any hours worked above 40 in a given
week. Write a program to input the number of hours worked and the hourly rate
and and calculate the total wages for the week."""

def main():

    print("This program accepts the number of hours worked and the hourly \
rate.")
    print("The program calculates the wages earned in a week with overtime \
at over 40 hours being paid time-and-a-half.\n")
    try:
        hours = float(input("Please enter the number of hours worked in the week: "))
        wage = float(input("Please enter the hourly wage: "))
        overtimePay = 1.5 * wage

        if hours >= 40:
            overtime = hours - 40
        else:
            overtime = 0

        pay = wage * (hours - overtime) + overtimePay * overtime

        print("The pay for this week is ${0:0.2f}.".format(pay))
    except (ValueError, SyntaxError):
        print("Please put in a number value. Exiting.")

main()
