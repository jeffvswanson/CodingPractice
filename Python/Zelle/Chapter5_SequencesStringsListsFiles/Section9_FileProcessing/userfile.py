# userfile.py
# Program to create a file of usernames in batch mode.

def main():
    
    print("This program creates a file of usernames from a")
    print("file of names.")

    # Get the file names
    infileName = input("What file are the names in? ")
    outfileName = input("What file should the usernames go in? ")

    # Open the file
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    # Process each line of the input file
    for line in infile:
        # Get the first and last names from line
        first, last = line.split()
        # Create the username
        uname = (first[0] + last[:7]).lower()
        # write it to the output file
        print(uname, file = outfile)

    # Close both files
    infile.close()
    outfile.close()

    print("Usernames have been written to", outfileName)

main()
