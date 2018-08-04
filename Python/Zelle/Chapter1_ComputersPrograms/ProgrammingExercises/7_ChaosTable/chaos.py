# File: chaos.py
# A simple program illustating chaotic behavior.
"""(Advanced) Modify the chaos program so that it accepts two inputs and then
prints a table with two columns similar to the one shown in section 1.8. (Note:
You will probably not be able to get the columns to line up as nicely as those
in the example. Chapter 5 discusses how to print numbers with a fixed number of
decimal places."""

def main():
    print("This program illustates a chaotic function")
    x = eval(input("Enter a number, x, between 0 and 1: "))
    y = eval(input("Please enter a second number, y, between 0 and 1: "))
    xString = "x"
    yString = "y"
    print(xString.center(12), yString.center(10))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print("{0:0.8f}  {1:0.8f}".format(x, y))

main()

