# approximatePi.py
# This program attempts to approximate pi based off a number of iterations
# and provides an accuracy check for the user.
"""Write a program that approximates the value of pi by summing the terms of
this series: 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...
The program should prompt the user for n, the number of terms to sum, and then
output the sum of the first n terms of the series. Have your program subtract
the approcimation from the value of math.pi to see how accurate it is."""

import math

def main():

    print("This propram attempts to approximate pi over a number of iterations and provids an accuracy check for the user.")

    n = int(input("Please enter the number of iterations you want to conduct: "))
    sumPositive = 0
    sumNegative = 0
    n = n * 2

    for i in range(1, n, 4):

        positives = 4/i
        sumPositive = sumPositive + positives

    for j in range(3, n, 4):

        negatives = 4/j
        sumNegative = sumNegative + negatives

    approximatePi = sumPositive - sumNegative

    accuracy = math.pi - approximatePi
    
    print("Your approximate value of pi is {0} and you are off by {1}."\
          .format(approximatePi, accuracy))
    
    
main()
