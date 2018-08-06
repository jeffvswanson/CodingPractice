# heatingAndCoolingDays.py
# A program that accepts a sequence of average daily temps and computes the 
# running # total of cooling and heating degree-days and prints the two totals
# after all data has been processed.
# Assume entries in the file are correctly formatted.
"""Modify Programming Exercise 11 to get its input from a file."""

def getFile():
    # Get the file name
    while True:
        try:
            infileName = input("\nPlease enter your file name: ")
        except (SyntaxError, NameError, TypeError, ValueError):
            print("You have to enter a file name.")
            continue
        break
    return infileName

def degreeDays(infileName):

    infile = open(infileName, "r")

    heatday = 0
    coolday = 0
    for line in infile:
        temp = float(line)

        if temp < 60:
            heatday = heatday + (60 - temp)
        elif temp > 80:
            coolday = coolday + (temp - 80)

    return heatday, coolday

def main():

    print("This program determines the number of heating and cooling days from \
a file.")

    infileName = getFile()
    # Send the file to get the heating degree days (hdd) and cooling degree
    # days (cdd).
    hdd, cdd = degreeDays(infileName)

    print("\nThe number value of heating degree days is {0:.1f}".format(hdd))
    print("The number value of cooling degree days is {0:.1f}".format(cdd))

main()
