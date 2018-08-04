# futvalTable.py
# A program to compute the value of an investment carried years into the future.
"""Write an improved version of the futval.py program from Chapter 2. Your
program will prompt the user for the amount of the investment, the annualized
interest rate, and the number of years of the investment. The program will then
output a nicely formatted table that tracks the value of the investment year by
year. Your output might look something like this:

Year    Value
---------------
  0    $2000.00
  1    $2200.00
  ...
  7    $3897.43"""

def main():
    print("This program calculates the future value of an x-year investment.")

    principal = float(input("Enter the intial principal: "))
    principalNaught = principal
    time = int(input("Enter the total number of years of the investment: "))
    apr = float(input("Enter the annual interest rate as a decimal: "))
    valueList = [principalNaught]

    for i in range(time + 1):
        principal = principal * (1 + apr)
        valueList.append(principal)

    # Print a table of the value of the investment by year.
    # Assume I don't need to adjust the table dynamically.
    print("Year       Value")
    print("----------------")

    for i in range(time + 1):
        print("{0:3}".format(i) + "${0:0.2f}".format(valueList[i]).rjust(13))
        
main()
