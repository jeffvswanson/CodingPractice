# fiveClickHouse.pyw
"""You are to write a program that allows the user to draw a simple house using
five mouse clicks. The first two clicks will be the opposite corners of the
rectangular frame of the house. The third click will indicate the center of the
top edge of a rectangular door. The door should have a total width that is 1/5
 of the width of the house frame. The sides of the door should extend down to
 the bottom of the frame. The fourth click will indicate the center of a square
 window. The window is half as wide as the door. The last click will indicate
 the peak of the roof. The edges of the roof will extend from the point at the
 peak to the corners of the top edge of the house frame."""

from graphics import *

def main():

    # Introduction
    print("This program allows the user to draw a simple house using five \
mouse clicks. The first two clicks will be the opposite corners of the \
rectangular frame of the house. The third click will indicate the center of \
the top edge of a rectangular door. The door should have a total width that is \
1/5 of the width of the house frame. The sides of the door should extend down \
to the bottom of the frame. The fourth click will indicate the center of a \
square window. The window is half as wide as the door. The last click will \
indicate the peak of the roof. The edges of the roof will extend from the \
point at the peak to the corners of the top edge of the house frame.")

    # Create a graphics window to build the house.
    win = GraphWin("Five-click House", 1000, 1000)
    win.setBackground("white")
    win.setCoords(0.0, 0.0, 100.0, 100.0)

    # Get and draw the user input for the frame
    messageCenter = Point(50, 99)
    message = Text(messageCenter, "Click the lower left portion of the house \
frame.")
    message.draw(win)
    p1 = win.getMouse()
    p1.draw(win)
    message.undraw()
    message = Text(messageCenter, "Click the upper right portion of the house \
frame.")
    message.draw(win)
    p2 = win.getMouse()
    frame = Rectangle(p1, p2)
    frame.draw(win)
    message.undraw()

    # Get and draw the user input for the door
    message = Text(messageCenter, "Click the center of the top edge of the \
door of the house.")
    message.draw(win)
    p3 = win.getMouse()
    doorWidth = (p2.getX() - p1.getX())/5
    # Door lower left corner point
    doorLLX = p3.getX() - (doorWidth/2)
    doorLL = Point(doorLLX, p1.getY())
    # Door upper right corener point
    doorURX = p3.getX() + (doorWidth/2)
    doorUR = Point(doorURX, p3.getY())
    door = Rectangle(doorLL, doorUR)
    door.draw(win)
    message.undraw()

    # Get the user input for the window and draw it
    message = Text(messageCenter, "Click where you want the window centered.")
    message.draw(win)
    p4 = win.getMouse()
    windowWidth = doorWidth/2
    # Window lower left corner point
    windowLLX = p4.getX() - (windowWidth/2)
    windowLLY = p4.getY() - (windowWidth/2)
    windowLL = Point(windowLLX, windowLLY)
    # Window upper right corner point
    windowURX = p4.getX() + (windowWidth/2)
    windowURY = p4.getY() + (windowWidth/2)
    windowUR = Point(windowURX, windowURY)
    window = Rectangle(windowLL, windowUR)
    window.draw(win)
    message.undraw()

    # Get the user input for the roof and draw it
    message = Text(messageCenter, "Click where you want the peak of the roof.")
    message.draw(win)
    p = win.getMouse()
    # Roof left anchor point
    roofLeft = Point(p1.getX(), p2.getY())
    roofLeftSlope = Line(roofLeft, p)
    roofLeftSlope.draw(win)
    roofRightSlope = Line(p2, p)
    roofRightSlope.draw(win)
    message.undraw()

    # Allow the user to close the window.
    message = Text(messageCenter, "Click anywhere to quit.")
    message.draw(win)
    win.getMouse()
    win.close()

main()
