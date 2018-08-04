# rectangleInformation.pyw
# This program displays information about a rectangle drawn by the user.
"""
Input: Two mouse clicks on opposite corners of a rectangle.
Output: Draw the rectangle.
    Print the perimeter and area of the rectangle.
Formulas: area = (length)(width)
    perimeter = 2(length + width)"""


from graphics import *

def main():

    # Introduction
    print("This program displays information about a rectangle.")

    # Create a graphics window to get the user generated rectangle.
    win = GraphWin("Rectangle Information", 400, 400)
    win.setBackground("white")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5.0, 0.5), "Click twice to place the rectangle.")
    message.draw(win)

    # Get and draw the user input for the rectangle.
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    rect = Rectangle(p1, p2)
    rect.draw(win)

    # Calculate the length
    l = p2.getX() - p1.getX()

    # Calculate the width
    w = p2.getY() - p1.getY()

    # Calculate the area
    a = l * w
    print("The area, A, of the rectangle is {:0.2f} units.".format(a))

    # Calculate the perimeter
    p = 2 * (l + w)
    print("The perimeter, P, of the rectangle is {:0.2f} units.".format(p))
        
    # Wait for another click to exit.
    message.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()

main()
