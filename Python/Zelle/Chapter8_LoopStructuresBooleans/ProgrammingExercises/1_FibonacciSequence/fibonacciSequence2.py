# fibonaccisequence2.py
# This program sums numbers in a Fibonacci sequence to a point specified by the
# user.
"""The Fibonacci sequence starts 1, 1, 2, 3, 5, 8,... Each number in the 
sequence (after the first two) is the sum of the previous two. Write a program
that computes and outputs the nth Fibonacci number, where n is a value entered
by the user."""

<<<<<<< HEAD
def getInput():
    try:
        n = int(input("Please input how many numbers you wish to proceed down \
the sequence: "))
    except (SyntaxError, NameError, TypeError, ValueError) as err:
        print("You have to enter a whole number. Exiting.")
        print(err.args)
        quit(0)
    return n

=======
>>>>>>> 9df6db465f2855ee3d149aa825ffa491706f03a7
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

<<<<<<< HEAD
    n = getInput()
=======
    try:
        n = int(input("Please input how many numbers you wish to proceed down \
the sequence: "))
    except (SyntaxError, NameError, TypeError, ValueError) as err:
        print("You have to enter a whole number. Exiting.")
        print(err.args)
        quit(0)
>>>>>>> 9df6db465f2855ee3d149aa825ffa491706f03a7
    fibNum = fibonacciNumber(n)
    
    print("The Fibonacci number for n = {0} is {1}.".format(n, fibNum))                
main()
