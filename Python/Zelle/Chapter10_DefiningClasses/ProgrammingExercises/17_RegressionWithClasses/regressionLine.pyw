# regressionLine.pyw
# Program graphically plots a regressions line after a user has put in all 
# points via mouse clicks.
"""Redo the regression problem from Chapter 8 (Programming Exercise 13) using a
Regression class. Your new class will beep track of the various quantities that
are needed to compute a line of regression (the running sums of x, y, x^2, and 
xy). The Regression class should have the following methods:
__init__ Creates a new regression object to which points can be added.
addPoint Adds a point to the regression object.
predict Accepts a value of x as a parameter, and returns the value of the 
    corresponding y on the line of best fit.
Note: Your class might also use some internal helfer methods to do such things
as compute the slope of the regression line."""

from graphics import *
from regressionClass import Regression

def createWindow():
    win = GraphWin("Linear Regression Chart", 500, 550)
    # xU is the upper bound of the x-coodinate system
    # Used to help draw the x-axis and line of regression
    xU = 50.0
    win.setCoords(0.0, 0.0, xU, 55.0)
    win.setBackground("white")
    
    yaxis = Line(Point(5, 5), Point(5, 50))
    yaxis.draw(win)
    Text(Point(4, 50), "y").draw(win)

    # Set up the x-axis endpoints based off the coordinate system
    xL = 0.1 * xU
    xR = xU - (0.1 * xU)
    xaxis = Line(Point(xL, 5), Point(xR, 5))
    xaxis.draw(win)
    Text(Point(46, 5), "x").draw(win)

    quitbutton = Rectangle(Point(1, 4.5), Point(11, 0.5))
    quitbutton.setFill("gray")
    quitbutton.setOutline("black")
    quitbutton.draw(win)
    quitmessage = Text(Point(6, 2.5), "Done")
    quitmessage.draw(win)

    return win, xL, xR

def getPoints(win, regressionLine):
    p = Point(0, 0)

    message = Text(Point(25, 27.5), "Please click inside the axis area").draw(win)
    # Test if the click is in the "Done" box
    while not((p.getX() >= 1 and p.getX() <= 11) and (p.getY() >= 0.5 and p.getY() <= 4.5)):
        p = win.getMouse()
        message.undraw()
        if p.getX() < 5 or p.getX() > 45 or p.getY() < 5 or p.getY() > 50:
            message.draw(win)
        else:
            message.undraw()
            p.draw(win)
            regressionLine.addPoint(p)
    message.undraw()
    return

def main():

    # Create the graphics window
    # Create a small rectangle labeled done.
    # Ask for user input
    # Create a decision loop for the user generated mouse clicks
    # Record each click in a list and track sum of x, y, x^2, and xy and number of clicks
    # If the mouseclick is in the "Done" box leave the loop and don't record the click
    # Calculate the linear regression from the list 
    # Plot the linear regression
    # Wait for a final mouseclick to close the window

    win, xL, xR = createWindow()
    regressionLine = Regression(win)
    getPoints(win, regressionLine)
    
    regressionLine.drawLine(xL, xR)
    
    message = Text(Point(25, 52.5), "Click anywhere to quit.")
    message.draw(win)
    win.getMouse()
    win.close()

main()
