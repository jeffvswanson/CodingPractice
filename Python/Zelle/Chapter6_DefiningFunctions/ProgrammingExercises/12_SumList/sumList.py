# sumList.py
# A program that asks for a list of numbers, then sums up the list.
"""Write and test a function to meet this specification.

sumList(nums) nums is a list of numbers. Return the sum of the numbers in the
list."""

def sumList(nums):
    summed = 0
    for entry in nums.split():
        num = float(entry)
        summed = summed + num
    return summed

def main():

    print("This program asks for a list of numbers then sums up the list.")
    nums = input("Please enter your list of numbers with a space between each \
entry: ")
    
    summedUp = sumList(nums)

    print("The sum of the list is: {0}.".format(summedUp))

main()
