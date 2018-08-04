# archeryTarget.pyw
# A program which draws an archery target.
"""An archery target consists of a central circle of yellow surrounded by
concentric rings of red, blue, black, and white. Each ring has the same witdth,
which is the same as the radius of the yellow circle. Write a program that draws
such a target. Hint: Object drawn later will appear on top of objects drawn
earlier."""

from graphics import *

def main():

    win = GraphWin("Archery Target")
    win.setCoords(0.0, 0.0, 12.0, 12.0)
    
    whiteRing = Circle(Point(6, 5), 5)
    whiteRing.setOutline("white")
    whiteRing.setFill("white")
    whiteRing.draw(win)
    
    blackRing = Circle(Point(6, 5), 4)
    blackRing.setOutline("black")
    blackRing.setFill("black")
    blackRing.draw(win)
    
    blueRing = Circle(Point(6, 5), 3)
    blueRing.setOutline("blue")
    blueRing.setFill("blue")
    blueRing.draw(win)
    
    redRing = Circle(Point(6, 5), 2)
    redRing.setOutline("red")
    redRing.setFill("red")
    redRing.draw(win)

    yellowRing = Circle(Point(6, 5), 1)
    yellowRing.setOutline("yellow")
    yellowRing.setFill("yellow")
    yellowRing.draw(win)
    
    message = Text(Point(6, 11.5), "Click anywhere to quit.")
    message.draw(win)
    win.getMouse()
    win.close()
    
main()
