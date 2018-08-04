# sumSeries
# This program sums a range of numbers entered by the user.
"""Write a program to sum a series of numbers entered by the user. The program
should first prompt the user for how many numbers are to be summed. The program
should then prompt the user for each of the numbers in turn and print out a
total sum after all the numbers have been entered. Hint: Use an input statement
in the body of the loop."""

def main():

    print("This program sums a series of numbers entered by the user.")

    n = int(input("Please input the amount of numbers you wish to sum: "))
    sum = 0

    for i in range(n):

        x = float(input("Please input the number you wish to add to the sum: "))
        ans = sum + x
        sum = ans

    print("The sum from is {:.0f}.".format(ans))
    
main()
