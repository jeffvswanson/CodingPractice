# squareClick.pyw
# A program which generates more squares as you click.
"""Make a program that:
(a) Draws squares.
(b) Each successive click draws an additional square on the screen (rather than
moving the existing one).
(c) Prints a message on the window "Click again to quit" after the loop, and
wait for a final click before closing the window."""

from graphics import *

def main():

    win = GraphWin()
    shape = Rectangle(Point(20, 20), Point(40, 40))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    for i in range(10):
        p = win.getMouse()
        dx = p.getX()
        dy = p.getY()
        newshape = Rectangle(Point(dx, dy), Point(dx+20, dy+20))
        newshape.setOutline("red")
        newshape.setFill("red")
        newshape.draw(win)

    message = Text(Point(100, 180), "Click again to quit.")
    message.draw(win)
    win.getMouse()
    win.close()

main()
