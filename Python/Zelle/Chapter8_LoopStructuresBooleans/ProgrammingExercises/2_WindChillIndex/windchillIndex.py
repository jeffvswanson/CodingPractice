# windchillIndex.py
# A program which calculates the windchill in Fahrenheit.
"""The National Weather Service computes the windchill index using the 
following formula:
    35.74 + 0.6215T - 35.75(V^0.16) + 0.4275T(V^0.16)
Where T is the temperature in degrees Fahrenheit, and V is the wind speed in 
miles per hour. Write a program that prints a nicely formatted table of 
windchill values. Rows should represent wind speed for 0 to 50 in 5-mph 
increments, and the columns represent temperatures from -20 to +60 in 10-degree
increments. Note: The formula only applies for wind speeds in excess of 3 miles
per hour."""

def listSetup():
    velocity = []
    temp = []
    windchill = []
    # Create a list of wind speeds from 0 to 50-mph in 5-mph increments
    for v in range(0, 51, 5):
        velocity.append(v)
    # Create a list of temperatures from -20 to 60 degrees Fahrenheit
    for t in range(-20, 61, 10):
        temp.append(t)
    # Iterate through the velocity list, then the temperature list to create
    # sequences of temperatures for a given wind speed.
    for v in velocity:
        if v > 3:
            for t in temp:
                chill = 35.74 + 0.6215*t - 35.75 * (v ** 0.16) + 0.4275 * t \
                * (v ** 0.16)
                windchill.append(chill)
        else:
            for t in temp:
                windchill.append(t)
    return velocity, windchill
    

def main():

    # Create lists for wind velocity, temperature range, and wind chill.
    vel, chill = listSetup()

    # Create the table header.
    print("Wind Speed (mph)| -20F| -10F|  0F | 10F | 20F | 30F | 40F | 50F |\
 60F |", end = "")

    # Create the table. Each row has slices 9 values from the windchill list
    a = 0
    for v in vel:
        print("\n{0:>16}|".format(v), end = "", flush = True)
        for c in chill[a:(a+9)]:
            print("{0:^5.0f}|".format(c), end = "", flush = True)
            a = a + 1
main()
