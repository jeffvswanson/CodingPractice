# average1.py
# A program which calculates the average of n numbers.

def main():
    n = int(input("How many numbers do you have to average? "))
    total = 0.0
    for i in range(n):
        x = float(input("Enter a number: "))
        total = total + x
    print("\nThe average of the numbers is", total/n)

main()
