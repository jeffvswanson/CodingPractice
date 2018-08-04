# futvalBatchFile.py
# This file reads a file and then outputs the values to a table in a new file.
"""Redo any of the previous programming problems to make them batch-oriented
(using text files for input and output)."""

def main():

    print("This program creates a file of future values from \
a file with principal, interest, and time.")

    # Get the file names
    infileName = input("What file are the values in? ")
    outfileName = input("What file should the future values go in? ")

    # Open the file
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    # Process each line of the input file
    for line in infile:
        # Get the principal, interest, and time values from line
        principal, time, apr = line.split()
        principal = float(principal)
        principalNaught = principal
        time = int(time)
        apr = float(apr)
        valueList = [principalNaught]

    for i in range(time + 1):
        principal = principal * (1 + apr)
        valueList.append(principal)

    # Write to the output file
    print("Year       Value", file = outfile)
    print("----------------", file = outfile)
    for i in range(time + 1):
        print("{:>4}".format(i) + "${0:0.2f}".format(valueList[i]).rjust(13),\
              file = outfile)

    # Close both files
    infile.close()
    outfile.close()

    print("The values of an investment over time have been \
written to {0}".format(outfileName))
        
    

main()
