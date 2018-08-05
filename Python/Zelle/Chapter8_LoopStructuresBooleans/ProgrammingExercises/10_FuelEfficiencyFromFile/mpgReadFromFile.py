# mpgReadFromFile.py
# A program that computes the fuel efficiency of a multi-leg journey from a 
# seperate file. Assume infor in the file is formatted correctly.
"""Modify Programming Exercise 9 to get its input from a file."""

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

def readFile(infileName):
    # Open the file
    infile = open(infileName, "r")

    legLength = []
    legFuel = []

    # Process each line of the input file to convert it to a list.
    for i, line in enumerate(infile):
        if i == 0:
            legLength.append(float(line))
            continue
        info = line.split()
        leg, fuel = float(info[0]), float(info[1])

        legLength.append(leg)
        legFuel.append(fuel)
        
    return legLength, legFuel
    
def calcMPG(legLength, legFuel):
    # Get and print the miles per gallon for each leg of the trip.
    i = 0 # Accumulator variable for list
    l = len(legLength)
    for entry in legLength:
        # Make sure the accumulator, i, is not out of the list's length
        if i + 1 < l:
            dist = legLength[i+1] - entry
            fuel = legFuel[i]
            mpg = dist / fuel

            print("Leg {0}: The MPG for this {1} mile leg is {2:0.1f} mpg."\
                .format(i+1, dist, mpg))

            i += 1
        else:
            break
    # Get and print the miles per gallon for the entire trip.
    dist = legLength[-1] - legLength[0]
    # Reset the fuel variable to sum the entire list.
    fuel = 0
    for entry in legFuel:
        fuel = fuel + entry
    mpg = dist / fuel

    return dist, mpg

def main():

    print("This program reads the distance and fuel used to calculate the fuel \
efficiency of the overall trip and each leg.")

    infileName = getFile()
    # Get the odometer readings and fuel used.
    legLength, legFuel = readFile(infileName)
    # Calculate and print the leg distance and mpg
    # Return the overall mpg and distance
    dist, mpg = calcMPG(legLength, legFuel)
            
    print("The overall MPG for this {0} mile trip is {1:0.1f} mpg."\
        .format(dist, mpg))

main()
