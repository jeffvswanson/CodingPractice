# mpg.py
# A program that computes the fuel efficiency of a multi-leg journey.
"""Write a program that computes the fuel efficiency of a multi-leg journey.
The program will first prompt for the starting odometer reading and then get
information about a series of legs. For each leg, the user enters the current
odometer reading and the amount of gas used (seperated by a space). The user 
signals the end of the trip with a blank line. The program should print out
the miles per gallon achieved on each leg and the total MPG for the trip.""" 

def getInput():
    legLength = []
    legFuel = []
    
    while True:
        try:
            leg = float(input("Please enter the initial odometer reading: "))
            legLength.append(leg)
        except (SyntaxError, NameError, TypeError, ValueError):
            print("You have to enter a whole number zero or greater.")
            continue
        if leg >= 0:
            break
        else:
            print("You have to enter a whole number zero or greater.")

    # Get the leg lengths and fuel used per leg
    while leg != "":
        info = input("Please enter the ending odometer reading for this leg \
of the journey and the fuel used seperated by a space (<Enter> to quit): ")\
.split(" ")
        if "" in info: break
        try:
            leg, fuel = float(info[0]), float(info[1])
        except (SyntaxError, NameError, TypeError, ValueError, IndexError):
            print("You have to enter your numbers seperated by a space.")
            continue
        if leg < 0 or fuel < 0:
            print("You can't travel negative distance or gain fuel.")
            continue
        else:
            legLength.append(leg)
            legFuel.append(fuel)

    # Check if legFuel is empty and exit the program
    if legFuel == []:
        print("Exiting.")
        quit(0)

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

            print("Leg {0}: The MPG for this {1} mile leg is {2:0.1f}."\
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
    # Get the odometer readings and fuel used
    legLength, legFuel = getInput()
    # Calculate and print the leg distance and mpg
    # Return the overall mpg and distance
    dist, mpg = calcMPG(legLength, legFuel)
            
    print("The overall MPG for this {0} mile trip is {1:0.1f}."\
        .format(dist, mpg))

main()
