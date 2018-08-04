# fibonacciSequence.py
# This program sums numbers in a Fibonacci sequence
# to a point specified by the user.
"""A Fibonacci sequence is a sequence of numbers where each successive number is
the sum of the previous two. The classic Fibonacci sequence begins:
1, 1, 2, 3, 5, 8, 13, ... Write a program that computes the nth Fibonacci number
where n is a value input by the user. For example, if n = 6, then the result is
8."""

def main():

    print("This program sums a series of numbers to produce a \
Fibonacci sequence to a point specified by the user.")

    n = int(input("Please input how many numbers you wish to proceed down the \
sequence: "))
    ans = 1
    sum = 0

    for i in range(n):

        print(ans)
        ans = sum + ans
        sum = ans - sum
                
main()
