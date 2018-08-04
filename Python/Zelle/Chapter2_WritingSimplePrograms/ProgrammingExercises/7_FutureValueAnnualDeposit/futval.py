# futval.py
# A program to compute the value of an investment
# carried x years into the future.
"""Suppose you have an investment plan where you invest a certain fixed amount
every year. Modify futval.py to compute the total accumulation of your
investment. The inputs to the program will be the amount to invest each year,
the interest rate, and the number of years for the investment."""

def main():
    print("This program calculates the future value of an x-year investment.")

    principal = eval(input("Enter the intial principal: "))
    addition = eval(input("Enter the additional funds deposited yearly: "))
    time = eval(input("Enter the total number of years of the investment: "))
    apr = eval(input("Enter the annual interest rate as a decimal: "))

    for i in range(time):
        principal = (principal + addition) * (1 + apr)

    print("The value in", time, "years is: ${0:,.2f}".format(principal))

main()
