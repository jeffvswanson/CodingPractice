# randomWalkDrawn.py
# A program to calculate how many steps away from a starting point you will end
# at assuming each step has a chance to step forward, back, left, or right. The
# program creates a graph of the progress.
"""Write a graptical program to trace a random walk (see Chapter 9 Programming 
Exercises 12 and 13) in two dimensions. In this simulation you should allow the
step to be taken in any direction. You can generate a random direction as an 
angle off of the x axis.
    angle = random() * 2 * math.pi
The new x and y positions are then given by these formulas:
    x = x + cos(angle)
    y = y + sin(angle)
The program should take the number of steps as an input. Start your walker at
the center of a 100x100 grid and draw a line that traces the walk as it 
progresses."""

from random import random
from graphics import *
import math

def main():
    n = getInput()
    WalkingWindow(n)

def getInput():

    win = GraphWin("Get Number of Steps", 200, 200)
    win.setBackground("white")
    win.setCoords(0.0, 0.0, 2.0, 2.0)
    message = Text(Point(1, 1.5), """Please input the 
number of steps you 
want to take.""").draw(win)

    stepEntry = Entry(Point(1, 1), 5)
    stepEntry.setText("1")
    stepEntry.draw(win)

    button = Text(Point(1, 0.5), "Click here when done.")
    button.draw(win)
    Rectangle(Point(0.25, 0.25), Point(1.75, 0.75)).draw(win)

    # Initialize p to immediately execute while loop to stay open until "Done"
    # clicked
    p = Point(0, 0)
    while not((p.getX() >= 0.25 and p.getX() <= 1.75) and \
    (p.getY() >= 0.25 and p.getY() <= 0.75)):
    
        p = win.getMouse()
        # Do nothing if the click is not in the "Click when done" button
        if not((p.getX() >= 0.25 and p.getX() <= 1.75 and \
    p.getY() >= 0.25 and p.getY() <= 0.75)):
            pass
        else:
            try:
                n = int(stepEntry.getText())
            except (SyntaxError, NameError, TypeError, ValueError):
                message.setText("""You have to enter a 
positive whole number.""")
                stepEntry.setText("1")
                # You don't want the window closing inadvertently, so reset p.
                p = Point(0, 0)
                continue
            if n < 1:
                print("You have to take at least one step.")
                p = Point(0, 0)
                continue
    win.close()
    return n

def WalkingWindow(n):
    # Module creates the window where the walk will be displayed.

    win = GraphWin("A Random Walk", 400, 400)
    win.setBackground("white")
    win.setCoords(-200, -200, 200, 200)

    walkingBox = Rectangle(Point(-100, -100), Point(100, 100))
    walkingBox.setOutline("black")
    walkingBox.draw(win)

    quitButton = Rectangle(Point(-150, -75), Point(-100, -25))
    quitButton.setFill("gray")
    quitButton.setOutline("black")
    quitButton.draw(win)
    quitMessage = Text(Point(-125, -50), "Done")
    quitMessage.draw(win)

    p = Point(0, 0)
    # Set the origin at (0,0) then extend the line from there.
    p1 = Point(0, 0)
    p2 = Point(0, 0)
    for i in range(n):
        p = win.checkMouse()
        # Test if a click is in the "Done" box

        if p == None or not((p.getX() >= -150 and p.getX() <= -100) \
        and (p.getY() >= -75 and p.getY() <= -25)):
            stepX, stepY = goOnAWalk(n, p2.getX(), p2.getY())
            p2 = Point(stepX, stepY)
            walkLine = Line(p1, p2)
            # Draw the beginning and end points differently
            if not(i == 0 or i == (n-1)):
                walkLine.setOutline("Orange")
            else: 
                walkLine.setOutline("Black")
            walkLine.draw(win)
            p1 = p2
        else:
            break
    # Keep the window open until the user clicks the "Done" box
    while p == None or not((p.getX() >= -150 and p.getX() <= -100) \
    and (p.getY() >= -75 and p.getY() <= -25)):
        p = win.checkMouse()

    win.close()
    return

def goOnAWalk(n, x, y):
    # This module simulates each step of the walk. A random angle is made and
    # used to derive x and y coordinates for the walk.
    angle = random() * 2 * math.pi
    x = x + math.cos(angle)
    y = y + math.sin(angle)

    return x, y

if __name__ == '__main__': main()
