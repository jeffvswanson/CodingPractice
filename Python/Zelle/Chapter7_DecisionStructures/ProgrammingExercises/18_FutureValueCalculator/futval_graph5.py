# futval_graph5.py
"""Take a favorite programming problem from a previous chapter and add 
decisions and/or exception handling as required to make it a truly robust 
(will not crash on any inputs)."""

from graphics import *

def getNums():
    initialWin = GraphWin("Initial Conditions", 400, 400)
    initialWin.setBackground("white")
    initialWin.setCoords(0.0, 0.0, 4.0, 4.0)
    Text(Point(1, 3),"Initial principal: $").draw(initialWin)
    Text(Point(1.33, 2.5),"Annualized percentage rate: ").draw(initialWin)
    
    principalEntry = Entry(Point(2, 3), 6)
    principalEntry.setText("0.00")
    principalEntry.draw(initialWin)
    
    aprEntry = Entry(Point(2.67, 2.5), 5)
    aprEntry.setText("0.01")
    aprEntry.draw(initialWin)
    
    button = Text(Point(2, 1.5), "Plot it")
    button.draw(initialWin)
    Rectangle(Point(1, 1.0), Point(3, 2)).draw(initialWin)

    initialWin.getMouse()

    try:
        principal = float(principalEntry.getText())
    except (SyntaxError, NameError, TypeError, ValueError) as err:
        print("You have to enter a number for principal. Exiting.")
        print(err.args)
        quit(0)
    if principal <= 0:
        print("You have to enter a number greater than zero to make money. \
Exiting.")
        quit(0)

    try:
        apr = float(aprEntry.getText())
    except (SyntaxError, NameError, TypeError, ValueError) as err:
        print("You have to enter a number for the APR. Exiting.")
        print(err.args)
        quit(0)
    if apr < 0:
        print("Please enter a positive APR next time. Debt is depressing. \
Exiting.")
        quit(0)

    initialWin.close()
    return apr, principal

def plotGrowth(apr, principal):
    # Create a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 360, 360)
    win.setBackground("white")
    height = 36.0
    width = 36.0
    win.setCoords(0.0, 0.0, width, height)
    
    Text(Point(2.0, 4.0), "${:.0f}".format(principal)).draw(win)

    # Finding the max value over the time period to break the range into
    # five seperately scaled values.
    finalAmount = principal * ((1 + apr) ** 10)
    difference = finalAmount - principal
    intervals = 5
    yInterval = (height - 6.0)/intervals

    # Plot the scaled values on the y-axis.
    for i in range(1, intervals + 1):
        interval = principal + (0.2 * i * difference)
        y = yInterval * i
        Text(Point(2.0, (4 + y)), "${:.0f}".format(interval)).draw(win)

    # Draw bar for initial principal
    barHeight = 4.0
    barWidth = 2.5
    bar = Rectangle(Point(6.0, 4), Point(6.0 + barWidth, 4))
    bar.setFill("green")
    bar.setWidth(barWidth)
    bar.draw(win)

    # Draw bars for successive years
    for year in range(1, 10):
        # Calculate value for the next year
        principal = principal * (1 + apr)
        # Draw bar for this value, xll = x lower left corner
        xll = year * barWidth + 6.0
        barHeight = ((difference - (finalAmount - principal))\
                     / difference) * (height - 6)
        bar = Rectangle(Point(xll, 4), Point(xll + barWidth, (4 + barHeight)))
        bar.setFill("green")
        bar.setWidth(barWidth)
        bar.draw(win)

    Text(Point(18.0, 2.0), "Click anywhere to quit.").draw(win)
    win.getMouse()
    win.close()
    return

def main():

    #Introduction
    print("This program plots the growth of a 10-year investment.")

    # Create a graphics window to get principal and interest rate
    apr, principal = getNums()

    plotGrowth(apr, principal)

main()