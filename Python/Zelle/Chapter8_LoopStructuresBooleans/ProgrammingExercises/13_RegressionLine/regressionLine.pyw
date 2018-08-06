# regressionLine.pyw
# Program graphically plots a regressions line after a user has put in all 
# points via mouse clicks.
"""Write a program that graphically plots a regression line -- that is, the
line with the best fit through a collection of points. First, ask the user to
specify the data points by clicking on them in a graphics window. To find the 
end of the input, place a small rectangle labeled "Done" in the lower-left 
corner of the window; the program will stop gathering points when the user 
clicks inside that rectangle.
    The regression line is the line with the following equation:
    y = yAvg + m(x - xAvg)
    where m = (sum(xSubi*ySubi) - n*xAvg*yAvg)/(sum(xSubi^2)-n*xAvg^2)
xAvg is the mean of the x-values, yAvg is the mean of the y-values, and n is the
number of points.
    As the user clicks on points, the program should draw them in the graphics
window and keep track of the count of input values and the running sum of x, y,
x^2, and x*y values. When the user clicks inside the "Done" rectangle, the 
program then computes the value of y (using the equations above) corresponding
to the x values at the left and right edges of the window to compute the 
endpoints of the regression line spanning the window. After the line is drawn,
the program will pause for another mouse click before closing the window and 
quitting."""    

from graphics import *

def createWindow():
    win = GraphWin("Linear Regression Chart", 500, 550)
    win.setCoords(0.0, 0.0, 50.0, 55.0)
    win.setBackground("white")
    
    yaxis = Line(Point(5, 5), Point(5, 50))
    yaxis.draw(win)
    Text(Point(4, 50), "y").draw(win)

    xaxis = Line(Point(5, 5), Point(45, 5))
    xaxis.draw(win)
    Text(Point(46, 5), "x").draw(win)

    quitbutton = Rectangle(Point(1, 4.5), Point(11, 0.5))
    quitbutton.setFill("gray")
    quitbutton.setOutline("black")
    quitbutton.draw(win)
    quitmessage = Text(Point(6, 2.5), "Done")
    quitmessage.draw(win)

    return win

def getPoints(win):
    p = Point(0, 0)
    n, sumx, sumy, sumxsquared, sumxy = 0, 0, 0, 0, 0
    points = []
    message = Text(Point(25, 27.5), "Please click inside the axis area").draw(win)
    # Test if the click is in the "Done" box
    while not((p.getX() >= 1 and p.getX() <= 11) and (p.getY() >= 0.5 and p.getY() <= 4.5)):
        p = win.getMouse()
        message.undraw()
        if p.getX() < 5 or p.getX() > 45 or p.getY() < 5 or p.getY() > 50:
            message.draw(win)
        else:
            message.undraw()
            points.append(p)
            n += 1
            sumx = sumx + p.getX()
            sumy = sumy + p.getY()
            sumxsquared = sumxsquared + (p.getX()) ** 2
            sumxy = sumxy + (p.getX() * p.getY())
            p.draw(win)

    return n, sumx, sumy, sumxsquared, sumxy, message

def regressionLine(win, n, x, y, xsquared, xy):
    avgx = x / n
    avgy = y / n
    m = (xy - n * avgx * avgy)/(xsquared - n * avgx ** 2)

    x1 = 5
    x2 = 45

    y1 = avgy + m * (x1 - avgx)
    y2 = avgy + m * (x2 - avgx)

    lineOfRegression = Line(Point(x1, y1), Point(x2, y2))
    lineOfRegression.setOutline("orange")
    lineOfRegression.draw(win)

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

    win = createWindow()

    n, sumx, sumy, sumxsquared, sumxy, message = getPoints(win)
    # Undraw the last message from the while loop.
    message.undraw()
    
    regressionLine(win, n, sumx, sumy, sumxsquared, sumxy)
    
    message = Text(Point(25, 52.5), "Click anywhere to quit.")
    message.draw(win)
    win.getMouse()
    win.close()

main()
