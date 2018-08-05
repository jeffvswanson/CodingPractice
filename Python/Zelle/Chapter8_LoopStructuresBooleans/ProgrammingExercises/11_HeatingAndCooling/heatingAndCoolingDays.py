# heatingAndCoolingDays.py
# A prgoram that accrepts a sequence of average daily temps and computes the 
# running # total of cooling and heating degree-days and prints the two totals
# after all data has been processed.
"""Heating and cooling degree days are measures used by utility companies to 
estimate energy requirements. If the average temperature for a day is below 60,
then the number of degrees below 60 is added to the heating degree days. If the
temperature is above 80, the amount over 80 is added to the cooling degree days.
Write a program that accepts a sequence of average daily temperatures and
computes the running total of cooling and heating degree days. The program 
should print these two totals after all the data has been processed."""

def userInput():
    tempList = []
    while True:
        temp = input("Please enter the average temperature for the \
day. <Enter to quit>: ")
        if temp == "" and tempList == []:
            print("Exiting the program")
            quit(0)
        elif temp == "":
            break
        else:
            try:
                tempList.append(float(temp))
            except (SyntaxError, NameError, TypeError, ValueError):
                print("You have to enter a number.")
                continue
    return tempList

def calcDD(tempList):
    # Initialize the heating degree days and cooling degree days
    hdd, cdd = 0, 0

    for temp in tempList:
        if temp < 60:
            hdd = hdd + (60 - temp)
        elif temp > 80:
            cdd = cdd + (temp - 80)

    return hdd, cdd    

def main():

    print("This program determines the number of heating and cooling days.")
    # Get user input to create a daily average temperature list (tempList).
    tempList = userInput()
    # Send the temperature list to get the heating degree days (hdd) and 
    # cooling degree days (cdd).
    hdd, cdd = calcDD(tempList)
        
    print("\nThe number value of heating degree days is {0:.1f}".format(hdd))
    print("The number value of cooling degree days is {0:.1f}".format(cdd))

main()
