# circleIntercepts.pyw
"""Do Programming Exercise 7 from Chapter 4, but add a decision to hangle the
case where the line does not intersect the circle."""

from graphics import *
import math

def getRadius():
    
    radiuswin = GraphWin("Get Circle Radius", 200, 200)
    radiuswin.setBackground("white")
    radiuswin.setCoords(0.0, 0.0, 2.0, 2.0)
    Text(Point(1, 1.5), "Circle radius, r (0 < r <= 10)").draw(radiuswin)

    radiusentry = Entry(Point(1, 1), 3)
    radiusentry.setText("1")
    radiusentry.draw(radiuswin)

    button = Text(Point(1, 0.5), "Enter y-intercept")
    button.draw(radiuswin)
    Rectangle(Point(0.25, 0.25), Point(1.75, 0.75)).draw(radiuswin)

    radiuswin.getMouse()
    
    try:
        radius = float(eval(radiusentry.getText()))
    except (ValueError, SyntaxError) as err:
        print("You have to enter a number. Exiting")
        print(err.args)
        quit(0)

    radiuswin.close()

    return radius

def getIntercept(radius):
    
    linewin = GraphWin("Get y-intercept", 400, 200)
    linewin.setBackground("white")
    linewin.setCoords(0.0, 0.0, 4.0, 2.0)
    Text(Point(2, 1.5), "Y-intercept must be between -{:-.2f} and {:-.2f}"
    .format(radius, radius)).draw(linewin)

    lineentry = Entry(Point(2, 1), 3)
    lineentry.setText("0")
    lineentry.draw(linewin)

    button = Text(Point(2, 0.5), "Find your intercepts")
    button.draw(linewin)
    Rectangle(Point(1, 0.25), Point(3, 0.75)).draw(linewin)

    linewin.getMouse()
    try:
        y = float(eval(lineentry.getText()))
    except (ValueError, SyntaxError) as err:
        print("You have to enter a number. Exiting.")
        print(err.args)
        quit(0)
    linewin.close()

    return y

def finalGraph(radius, yint, x1, x2):
           
    finalwin = GraphWin("X-intercept Graph", 550, 550)
    finalwin.setBackground("white")
    finalwin.setCoords(0.0, 0.0, 22.0, 22.0)

    xaxis = Line(Point(1, 11), Point(21, 11))
    xaxis.draw(finalwin)
    Text(Point(1, 10.5), "-10").draw(finalwin)
    Text(Point(21, 10.5), "10").draw(finalwin)
    
    yaxis = Line(Point(11, 1), Point(11, 21))
    yaxis.draw(finalwin)
    Text(Point(11.5, 21), "10").draw(finalwin)
    Text(Point(11.5, 1), "-10").draw(finalwin)

    circle = Circle(Point(11, 11), radius)
    circle.setOutline("blue")
    circle.draw(finalwin)

    line = Line(Point(0, 11 + yint), Point(22, 11 + yint))
    line.setOutline("orange")
    line.draw(finalwin)

    intercept1 = Circle(Point(11 + x1, 11 + yint), 0.25)
    intercept1.setOutline("red")
    intercept1.setFill("red")
    intercept1.draw(finalwin)

    intercept2 = intercept1.clone()
    intercept2.move(2 * x2, 0)
    intercept2.draw(finalwin)

    Text(Point(18, 21.0), "Click anywhere to quit.").draw(finalwin)
    finalwin.getMouse()
    finalwin.close()

def main():

    # Introduction
    print("""This program graphs a circle of radius, r, and a horizontal line.
The program shows the intercepts of the horizontal line with the circle and
prints the x-intercepts.""")

    # Create a graphics window to get the radius of the circle
    r = getRadius()

    # Create a graphics window to get a horizontal line intercepting the circle.
    y = getIntercept(r)

    # Draw the circle, line, and intercepts. Print the intercept values.
    if y > r:
        print("\nThe line does not intercept the circle.")
    else:
        x1 = math.sqrt(r**2 - y**2)
        x2 = -x1
        print("\nThe line intersects the circle at x = {:-.2f} and {:-.2f}"\
        .format(x2, x1))
        finalGraph(r, y, x1, x2)
        
main()
