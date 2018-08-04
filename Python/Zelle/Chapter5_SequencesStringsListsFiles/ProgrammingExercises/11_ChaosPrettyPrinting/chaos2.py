# File: chaos2.py
# A simple program illustating chaotic behavior.
"""Write an improved version of the chaos.py program from Chaper 1 that allows
a user to input two initial values and the number of iterations, and then
prints a nicely formatted table showing how the values change over time. For
example, if the starting values were .25 and .26 with 10 iterations, the table
might look like this:

index    0.25       0.26
--------------------------
  1   0.731250    0.750360
  2   0.766441    0.730547
...
 10   0.118509    0.974630"""

def main():
    print("This program illustates a chaotic function")
    x = float(input("Enter a number, x, between 0 and 1: "))
    y = float(input("Please enter a second number, y, between 0 and 1: "))
    indexString = "index {0:^12.2f} {1:^10.2f}".format(x, y)
    print(indexString)
    dashString = "-" * (1 + len(indexString))
    print(dashString)
    for i in range(1, 11):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print("{0:>3}    {1:0.8f}   {2:0.8f}".format(i, x, y))

main()

