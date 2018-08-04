# fibonaccisequence2.py
# This program sums numbers in a Fibonacci sequence to a point specified by the
# user.
"""Write a function to calculate the nth Fibonacci number. Use your function to
solve Programming Exercise 16 from Chapter 3."""

def fibonacciNumber(n):
    ans = 1
    sum = 0

    for i in range(n-1):

        print("n = {0}, {1}".format((i+1),ans))
        ans = sum + ans
        sum = ans - sum

    print("n = {0}, {1}".format(n,ans))
    return ans

def main():

    print("This program sums a series of numbers to produce a Fibonacci \
sequence to a point specified by the user.")

    n = int(input("Please input how many numbers you wish to proceed down the \
sequence: "))

    fibNum = fibonacciNumber(n)
    
    print("The Fibonacci number for n = {0} is {1}.".format(n, fibNum))
                
main()
