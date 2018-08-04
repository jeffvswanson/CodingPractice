# triangleInformation.pyw
# This program displays information about a triangle drawn by the user.
"""
Input: Three mouse clicks on vertices of a triangle.
Output: Draw the trangle.
    Print the perimeter and area of the triangle.
Formulas: For perimeter, see length from the Line Segment problem.
    area = sqrt(s(s - a)(s - b)(s - c)) where a, b, and c are the lengths of the
    sides and s = (a + b + c) / 2."""


from graphics import *
import math

def main():

    # Introduction
    print("This program displays information about a triangle.")

    # Create a graphics window to get the user generated triangle.
    win = GraphWin("Triangle Information", 400, 400)
    win.setBackground("white")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5.0, 0.5), "Click three times to place the triangle.")
    message.draw(win)

    # Get and draw the user input for the triangle.
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    a = Line(p1, p2)
    a.draw(win)
    b = Line(p2, p3)
    b.draw(win)
    c = Line(p3, p1)
    c.draw(win)

    # Calculate the lengths
    dxa = p2.getX() - p1.getX()
    dxb = p3.getX() - p2.getX()
    dxc = p1.getX() - p3.getX()
    
    dya = p2.getY() - p1.getY()
    dyb = p3.getY() - p2.getY()
    dyc = p1.getY() - p3.getY()
    
    a = math.sqrt(dxa**2 + dya**2)
    b = math.sqrt(dxb**2 + dyb**2)
    c = math.sqrt(dxc**2 + dyc**2)

    # Calculate the perimeter
    p = a + b + c
    print("The perimeter, P, of the triangle is {:0.2f} units".format(p))

    # Calculate s
    s = p/2

    # Calculate the area
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("The area, A, of the triangle is {:0.2f} units.".format(area))
        
    # Wait for another click to exit.
    message.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()

main()
