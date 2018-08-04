# File: chaos.py
# A simple program illustating chaotic behavior.
"""Modify the chaos program from section 1.6 so it prints out 20 values instead
of 10."""

def main():
    print("This program illustates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(20):
        x = 3.9 * x * (1 - x)
        print(x)

main()
