# futval.py
# A program to compute the value of an investment
# carried x years into the future.
"""Modify the futval.py program (section 2.7) so that the number of years
for the investment is also a user input. Make sure to change the final message
to reflect the correct number of years."""

def main():
    print("This program calculates the future value of an x-year investment.")

    principal = eval(input("Enter the intial principal: "))
    time = eval(input("Enter the total number of years of the investment: "))
    apr = eval(input("Enter the annual interest rate as a decimal: "))

    for i in range(time):
        principal = principal * (1 + apr)

    print("The value in", time, "years is: ${0:,.2f}".format(principal))

main()
