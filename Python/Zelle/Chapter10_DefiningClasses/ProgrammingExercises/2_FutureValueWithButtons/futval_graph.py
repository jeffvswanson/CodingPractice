# futval_graph.py
"""Use the Button class discussed in this chapter to build a GUI for one (or 
more) of your projects from previous chapters."""

from graphics import *
from button import Button

def getInputs():
    win = GraphWin("Initial Conditions", 400, 400)
    win.setBackground("white")
    win.setCoords(0.0, 0.0, 4.0, 4.0)
    Text(Point(1, 3),"Initial principal: $").draw(win)
    Text(Point(1.33, 2.5),"Annualized percentage rate: ").draw(win)
    
    principalEntry = Entry(Point(2, 3), 6)
    principalEntry.setText("0.00")
    principalEntry.draw(win)
    
    aprEntry = Entry(Point(2.67, 2.5), 5)
    aprEntry.setText("0.01")
    aprEntry.draw(win)
    
    plotButton = Button(win, Point(2, 1.5), 1, 0.5, "Plot it")
    plotButton.activate()
    p = Point(0, 0)
    # message is just a placeholder for error messages
    message = Text(Point(2, 0.5), "").draw(win)
    # Test the inputs for errors
    while plotButton.clicked(p) == False:
        p = win.getMouse()
        # Do nothing if the click is not in the "Plot it" button
        if plotButton.clicked(p) == False:
            pass
        else:
            message.setText("")
            try:
                principal = float(principalEntry.getText())
                # Principal must be positive
                if principal <= 0:
                    # Reset p to keep the window open
                    p = Point(0, 0)
                    message.setText("""You have to enter a positive 
    number greater than zero
    for the principal.""")
                    principalEntry.setText("0.00")
                    continue
            except (SyntaxError, NameError, TypeError, ValueError):
                message.setText("""You have to enter a positive
    number greater than zero
    for the principal.""")
                principalEntry.setText("0.00")
                p = Point(0, 0)
                continue
            try:    
                apr = float(aprEntry.getText())
                # APR must be positive
                if apr <= 0:
                    p = Point(0, 0)
                    message.setText("""You have to enter a positive 
    number greater than zero
    for the APR.""")
                    aprEntry.setText("0.01")
                    continue
            except (SyntaxError, NameError, TypeError, ValueError):
                message.setText("""You have to enter a positive
    number greater than zero
    for the APR.""")
                aprEntry.setText("0.01")
                p = Point(0, 0)
                continue

    win.close()
    return apr, principal

def plotFutureValue(apr, principal):
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

def main():
    #Introduction
    print("This program plots the growth of a 10-year investment.")
    # Create a graphics window to get principal and interest rate
    apr, principal = getInputs()
    # Create a graphics window with labels on left edge
    plotFutureValue(apr, principal)
main()
