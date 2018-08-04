# File: chaos.py
# A simple program illustating chaotic behavior.
"""Modify the chaos program from Section 1.6 using 2.0 in place of 3.9 as the
multiplier in the logistic function. Your modified line of code should look
like this:
        x = 2.0 * x * (1 - x)
Run the program for various input values and compare the results to those
obtained in the original program. Write a short paragraph describing any
differences that you notice in the behavior of the two versions."""

def main():
    print("This program illustates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 2.0 * x * (1 - x)
        print(x)

main()

"""Between the two programs the program from section 1.6 seems to continually
maintain an unstable state, whereas, this program seems to converge on 0.5. In
fact, if you put the value of 0.5 in this program never diverges and if you
choose a number above or below 0.5 the calculation converges to it or
extremely close within about 5 iterations."""
