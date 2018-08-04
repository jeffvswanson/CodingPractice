# numberAverage
# This program averages a range of numbers entered by the user.
"""Write a program that finds the average of a series of numbers entered by the
user. As in the previous problem, the program will first ask the user how many
numbers there are. Note: The average should always be a float, even if the user
inputs are all ints."""

def main():

    print("This proprams averages a series of numbers entered by the user.")

    n = int(input("Please input the amount of numbers you wish to sum: "))
    sum = 0

    for i in range(n):

        x = float(input("Please input the number you wish to add to the sum: "))
        ans = sum + x
        sum = ans

    average = sum / n
    print("The average of the numbers is {:.2f}".format(average))
    
main()
