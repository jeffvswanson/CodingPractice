# toNumbers.py
# A program which converts each entry in a list of strings representing numbers (text)
# to a recognized number (integer, float, etc.).
"""Write and test a function to meet this specification.

toNumbers(strList) strList is a list of strings, each of which represents a
number. Modifies each entry in the list by converting it to a number."""

def toNumbers(strList):
    numList = []
    for entry in strList.split():
        num = float(entry)
        numList.append(num)
    
    return numList

def main():

    print("This program asks for a list of numbers then onverts the string \
list to a type recognized as a number by python (int, float, etc.).\n")
    strList = input("Please enter the list of numbers seperated by a space. ")

    numList = toNumbers(strList)

    print(numList)

    print("The string list of numbers were converted to {0} in Python."
          .format(type(numList[0])))
          

main()
