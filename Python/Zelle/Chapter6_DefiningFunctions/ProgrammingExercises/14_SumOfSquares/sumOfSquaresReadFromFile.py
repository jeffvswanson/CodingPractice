# sumOfSquaresReadFromFile.py
# A program computes the sum of the squares of numbers read from a file.
"""Use the functions from the previous three  problems to implement a program
that computes the sum of the squares of numbers read from a file. Your program
should prompt for a file name and print out the sum of the squares of the values
in the file. Hint: Use readlines()"""

def toNumbers(fileData):
    numList = []
    for line in fileData:
        for entry in line.split():
            num = float(entry)
            numList.append(num)
    return numList

def squareEach(nums):
    squaredList = []
    for entry in nums:
        squaredNum = entry ** 2
        squaredList.append(squaredNum)
    return squaredList

def sumList(nums):
    summed = 0
    for entry in nums:
        summed = summed + entry
    return summed

def main():
    print("This program reads numbers from a file, squares each, sums them, \
and prints the output.")

    # Get the file name
    infileName = input("Please enter your file name: ")

    # Open the file
    infile = open(infileName, "r")

    # Process each line of the input file to convert it to a number type
    numList = toNumbers(infile)

    # Process the list to square each entry
    squaredList = squareEach(numList)

    # Sum the entries in the squaredList together
    summedUp = sumList(squaredList)

    print("The sum of the squares from {0} is {1}.".
          format(infileName, summedUp))

main()
