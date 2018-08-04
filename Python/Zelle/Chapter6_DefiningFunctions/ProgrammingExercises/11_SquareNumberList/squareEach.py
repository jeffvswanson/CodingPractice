# squareEach.py
# A program that asks for a list of numbers, then squares each entry.
"""Write and test a function to meet this specification.

squareEach(nums) nums is a list of numbers. Modifies the list by squaring each
entry."""

def squareEach(nums):
    squaredList = []
    for entry in nums.split():
        num = float(entry)
        squaredNum = num ** 2
        squaredList.append(squaredNum)

    return squaredList

def main():

    print("This program asks for a list of numbers then squares each entry in \
the list.")
    nums = input("Please enter your list of numbers with a space between each \
entry: ")

    squared = squareEach(nums)
    
    print("The square of each entry is:", squared)

main()
