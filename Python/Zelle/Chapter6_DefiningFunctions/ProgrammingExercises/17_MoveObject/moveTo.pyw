# moveTo.pyw
# A program that draws a circle then allows the user to click to move the circle
# ten times.
"""Write a function to meet this specification.

moveTo(shape, newCenter) shape is a graghics object that supports the getCenter
method and newCenter is a Point. Moves shape so that newCenter is its center.

Use your function to write a program that draws acircle and then allows the user
to click the window 10 times. Each time the user clicks, the circle is moved
where the user clicked."""

from graphics import *

def moveTo(shape, newCenter):

    oldCenter = shape
    newCircle = Circle(newCenter, 3)
    newCircle.setOutline("peachpuff")
    newCircle.setFill("peachpuff")

    return newCircle
    
def main():

    # Set the initial circle conditions
    win = GraphWin("Move your circle", 400, 400)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    center = Point(5, 5)
    firstCircle = Circle(center, 3)
    firstCircle.setOutline("peachpuff")
    firstCircle.setFill("peachpuff")
    firstCircle.draw(win)
    message = Text(Point(5, 0.5), "Click to move the circle.")
    message.draw(win)

    # Get and draw the new Circle.
    shape = firstCircle.getCenter()
    # Initialize oldCircle for the loop below
    oldCircle = Circle(center, 3)
    
    for i in range(10):
        newCenter = win.getMouse()
        firstCircle.undraw()
        oldCircle.undraw()
        newCircle = moveTo(shape, newCenter)
        newCircle.draw(win)
        oldCircle = newCircle
        shape = newCircle.getCenter()

    # Wait for another click to exit.
    message.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()
    
main()
