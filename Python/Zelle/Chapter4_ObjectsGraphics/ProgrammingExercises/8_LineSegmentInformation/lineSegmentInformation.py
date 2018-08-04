# lineSegmentInformation.pyw
# This is a program designed to allow the user to draw a line segment
# and then displays then displays the midpoint of the line segment in
# cyan and prints the length and slope of the line.
"""
Input: Two mouse clicks for the end points of the line segment.
Output: Draw the midpoint of the segment in cyan.
    Draw the line.
    Print the length and slope of the line.
Formulas: dx = x2 - x1
    dy = y2 - y1
    slope = dy/dx
    length = sqrt(dx^2 + dy^2)"""


from graphics import *
import math

def main():

    # Introduction
    print("""This program allows the user to draw a line segment. The
program marks the midpoint in a different color and prints the length
and slope of the line.""")

    # Create a graphics window to get the user generated line.
    win = GraphWin("Line Segment Length and Slope", 400, 400)
    win.setBackground("white")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5.0, 0.5), "Click on two points.")
    message.draw(win)

    # Get and draw the user input for the line segment.
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    line = Line(p1, p2)
    line.draw(win)

    midpoint = line.getCenter()
    midpoint.setOutline("cyan")
    midpoint.draw(win)

    # Calculate the change in x
    dx = p2.getX() - p1.getX()

    # Calculate the change in y
    dy = p2.getY() - p1.getY()

    # Calculate and display the slope
    slope = dy/dx
    print("The line segment slope, m, is {:0.2f}.".format(slope))

    # Calculate and dispaly the line segment length
    length = math.sqrt(dx**2 + dy**2)
    print("The line segment length, l, is {:0.2f}".format(length))
        
    # Wait for another click to exit.
    message.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()

main()
