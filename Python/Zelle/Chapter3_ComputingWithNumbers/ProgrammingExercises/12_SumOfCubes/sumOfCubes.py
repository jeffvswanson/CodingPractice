# sumOfCubes.py
# A program to calculate the sum of the cubes of the first n natural numbers
# where n is provided by the user.
"""Write a program fo find the sum of the cubes of the first n natural numbers
where the value of n is provided by the user."""

def main():

    print("This program calculates the sum of the cubes of the first n natural numbers where n is provided by the user.")
    n = int(input("Please enter how many numbers you want to add together: "))
    sum = 0
    ans = 0

    for i in range(n):

        ans = sum + i**3
        sum = ans     

    print(ans)
main()
