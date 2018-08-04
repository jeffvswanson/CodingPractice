# archeryScore.pyw
# A program which draws an archery target and scores the hits.
"""Archery Scorer. Write a program that draws an archery target (See 
Programming Exercise 2 from Chapter 4) and allows the user to click five times
to represent  arrows shot at the target. Using five-band scoring, a bulls-eye
(yellow) is worth 9 points and each successive ring is worth 2 fewer points
down to 1 for white. The program should output a score for each click and keep
track of a running sum for the entire series."""

from graphics import *
import math

def createTarget(win):
    
    whiteRing = Circle(Point(25, 25), 25)
    whiteRing.setOutline("white")
    whiteRing.setFill("white")
    whiteRing.draw(win)
    
    blackRing = Circle(Point(25, 25), 20)
    blackRing.setOutline("black")
    blackRing.setFill("black")
    blackRing.draw(win)
    
    blueRing = Circle(Point(25, 25), 15)
    blueRing.setOutline("blue")
    blueRing.setFill("blue")
    blueRing.draw(win)
    
    redRing = Circle(Point(25, 25), 10)
    redRing.setOutline("red")
    redRing.setFill("red")
    redRing.draw(win)

    yellowRing = Circle(Point(25, 25), 5)
    yellowRing.setOutline("yellow")
    yellowRing.setFill("yellow")
    yellowRing.draw(win)

def getPoints(win):

    points = []
    
    message = Text(Point(25, 53), "Click where the first arrow hit.")
    message.draw(win)
    p1 = win.getMouse()
    p1.draw(win)
    points.append(p1)

    message.setText("Click where the second arrow hit.")
    p2 = win.getMouse()
    p2.draw(win)
    points.append(p2)

    message.setText("Click where the third arrow hit.")
    p3 = win.getMouse()
    p3.draw(win)
    points.append(p3)

    message.setText("Click where the fourth arrow hit.")
    p4 = win.getMouse()
    p4.draw(win)
    points.append(p4)

    message.setText("Click where the final arrow hit.")
    p5 = win.getMouse()
    p5.draw(win)
    points.append(p5)

    message.setText("")
    
    return points

def getDistance(points):

    lengths = []
    center = Point(25.0, 25.0)

    for i in points:
       dx = i.getX() - center.getX()
       dy = i.getY() - center.getY()

       distance = math.sqrt(dx**2 + dy**2)

       lengths.append(distance)
       print(distance)

    return lengths

def getScore(lengths):

    score = 0
    for i in lengths:
        if i <= 5:
            score = score + 9
        elif i > 5 and i <= 10:
            score = score + 7
        elif i > 10 and i <= 15:
            score = score + 5
        elif i > 15 and i <= 20:
            score = score + 3
        elif i > 20 and i <=25:
            score = score + 1
        else:
            score = score

    return score

def main():

    win = GraphWin("Archery Target Score", 500, 550)
    win.setCoords(0.0, 0.0, 50.0, 55.0)
    
    createTarget(win)

    points = getPoints(win)

    lengths = getDistance(points)    

    score = getScore(lengths)

    scoreMessage = Text(Point(25, 51), "The score is {0}.".format(score))
    scoreMessage.draw(win)
    message = Text(Point(25, 53), "Click anywhere to quit.")
    message.draw(win)
    win.getMouse()
    win.close()
    
main()
