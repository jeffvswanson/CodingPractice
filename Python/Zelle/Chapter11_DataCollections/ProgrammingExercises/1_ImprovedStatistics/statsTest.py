# statsTest.py
"""Modify the statistics program from this chapter so that client programs have
more flexibility in computing the mean and/or standard deviation. Specifically,
redesign the library to have the following functions:

mean(nums) Returns the mean of numbers in nums.
stdDev(nums) Returns the standard deviation of nums.
meanStdDev(nums) Return both the mean and standard deviation of nums."""

from statsClass import Statistics

def getNumbers():
    nums = [] # Start with an empty list
    # Sentinel loop to get numbers
    xStr = input("Enter a number (<Enter> to quit) >> ")
    while xStr != "":
        x = float(xStr)
        nums.append(x) # Add this value to the list
        xStr = input("Enter a number (<Enter> to quit)  >> ")
    return nums

def main():
    print("This program computes mean and standard deviation.")

    nums = Statistics(getNumbers())
    xbarAndStd = nums.meanStdDev()
    std = nums.stdDev()
    xbar = nums.mean()



    print("\nThe mean is", xbar)
    print("The standard deviation is", std)
    print("The mean and standard deviation is", xbarAndStd, "respectively.")

if __name__ == '__main__': main()