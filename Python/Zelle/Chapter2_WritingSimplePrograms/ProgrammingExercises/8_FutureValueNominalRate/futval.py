# futval.py
# A program to compute the value of an investment
# carried x years into the future.
"""As an alternative to APR, the interest accrued on an account is often
described in terms of a nominal rate and the number of compounding periods.
For example, if the interest rate is 3% and the interest is compounded
quarterly, the account actually earns 3/4% interest every 3 months.

Modify the futval.py program to use this method of entering the interest rate.
The program should prompt the user for the yearly rate (rate) and the number
of times that the interest is compounded each year (periods). To compute the
value in ten years, the program will loop 10 * periods times and accrue
rate/period interest on each iteration."""

def main():
    print("This program calculates the future value of an 10-year investment.")
    print("At a nominal interest rate and period selected by the user.")

    principal = eval(input("Enter the intial principal: "))
    time = 10 # years
    rate = eval(input("Enter the yearly interest rate as a decimal: "))
    period = eval(input("Enter the number of times compounded per year: "))

    for i in range(time*period):
        principal = principal * (1 + (rate/period))

    print("The value in", time, "years is: ${0:,.2f}".format(principal))

main()
