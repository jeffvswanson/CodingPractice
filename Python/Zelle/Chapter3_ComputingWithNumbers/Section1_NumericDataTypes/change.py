# change.py
# A program to calculate the value of some change in dollars.

def main():
    print("Change Counter")
    print()
    print("Please enter the count of each coin type.")
    quarters = eval(input("Quarters: "))
    dimes = eval(input("Dimes: "))
    nickles = eval(input("Nickels: "))
    pennies = eval(input("Pennies: "))
    total = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    print()
    print("The total value of your change is", total)

main()    
