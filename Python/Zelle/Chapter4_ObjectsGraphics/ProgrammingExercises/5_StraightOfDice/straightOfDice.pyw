# straightOfDice.pyw
# A program which draws a straight of dice: 1, 2, 3, 4, 5
"""Write a program that draws 5 dice  on the screen depicting a straight
(1,2,3,4,5 or 2,3,4,5,6)."""

from graphics import *

def main():

    win = GraphWin("Straight of Dice", 500, 90)
    win.setCoords(0.0, 0.0, 50.0, 9.0)

    dice = Rectangle(Point(3,2), Point(8, 7))
    dice.setOutline("black")
    dice.setFill("white")
    dice.draw(win)

    dot = Circle(Point(5.5, 4.5), 0.5)
    dot.setOutline("black")
    dot.setFill("black")
    dot.draw(win)

    dice2 = dice.clone()
    dice2.move(10, 0)
    dice2.draw(win)

    dot2a = dot.clone()
    dot2a.move(10, -1)
    dot2a.draw(win)

    dot2b = dot2a.clone()
    dot2b.move (0, 2)
    dot2b.draw(win)

    dice3 = dice.clone()
    dice3.move(20, 0)
    dice3.draw(win)

    dot3a = dot.clone()
    dot3a.move(19, -1)
    dot3a.draw(win)

    dot3b = dot3a.clone()
    dot3b.move(1, 1)
    dot3b.draw(win)

    dot3c = dot3b.clone()
    dot3c.move(1, 1)
    dot3c.draw(win)

    dice4 = dice.clone()
    dice4.move(30, 0)
    dice4.draw(win)

    dot4a = dot.clone()
    dot4a.move(29, -1)
    dot4a.draw(win)

    dot4b = dot4a.clone()
    dot4b.move(0, 2)
    dot4b.draw(win)

    dot4c = dot4a.clone()
    dot4c.move(2, 2)
    dot4c.draw(win)

    dot4d = dot4a.clone()
    dot4d.move(2, 0)
    dot4d.draw(win)

    dice5 = dice.clone()
    dice5.move(40, 0)
    dice5.draw(win)

    dot5a = dot.clone()
    dot5a.move(39, -1)
    dot5a.draw(win)

    dot5b = dot5a.clone()
    dot5b.move(0, 2)
    dot5b.draw(win)

    dot5c = dot5a.clone()
    dot5c.move(2, 2)
    dot5c.draw(win)

    dot5d = dot5a.clone()
    dot5d.move(1, 1)
    dot5d.draw(win)

    dot5e = dot5a.clone()
    dot5e.move(2, 0)
    dot5e.draw(win)

main()
