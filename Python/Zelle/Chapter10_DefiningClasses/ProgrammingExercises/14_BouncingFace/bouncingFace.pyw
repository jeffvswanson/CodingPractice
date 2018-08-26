# bouncingFace.pyw
# A program which animates a bouncing face around a window.
# When the face hits an edge the expression changes.
"""Modify the Face class from the previous problem to include a move method
similar to other graphics objects. Using the move method, create a program that
make a face bounce around in a window (See Programming Exercise 17 from 
Chapter 7). Bonus: have the face change expression each time it "hits" the edge
of the window."""

from graphics import *
from random import randrange
from time import sleep

from face import Face

def createWindow(winHeight, winLength):

    win = GraphWin("Bouncing Face Animation", winLength, winHeight, \
    autoflush = False)
    win.setCoords(0.0, 0.0, winLength, winHeight)

    return win

def changeFace(win, center, size, theFace):
    # Clear the face
    for item in win.items[:]:
        item.undraw()
    win.update()
    faceList = ["grim", "smile", "wink", "frown"]
    # Pick a random face to draw
    index = randrange(0, len(faceList))
    faceList[index]
    if faceList[index] == "grim":
        return theFace.grim(win, center, size)
    elif faceList[index] == "smile":
        return theFace.smile(win, center, size)
    elif faceList[index] == "wink":
        return theFace.wink(win, center, size)
    else:
        return theFace.frown(win, center, size)

def animateFace(win, height, length):

    size = (1/10) * height
    xCenter = length/2 - 1
    yCenter = height/2 - 1
    center = Point(xCenter, yCenter)

    animationLength = 1000
    dx = 1
    dy = 1
    theFace = Face(win, center, size)
    # Bounce the face around the window.
    for i in range(animationLength):
        if (theFace.head.getCenter().getX() + size) + dx >= length:
            dx = -1
            center = theFace.head.getCenter()
            changeFace(win, center, size, theFace)
        elif (theFace.head.getCenter().getX() - size) - dx <= 0:
            dx = 1
            center = theFace.head.getCenter()
            changeFace(win, center, size, theFace)

        if (theFace.head.getCenter().getY() + size) + dy >= height:
            dy = -1
            center = theFace.head.getCenter()
            changeFace(win, center, size, theFace)
        elif (theFace.head.getCenter().getY() - size) - dy <= 0:
            dy = 1
            center = theFace.head.getCenter()
            changeFace(win, center, size, theFace)

        theFace.moveFace(height, length, size, dx, dy)
        update(60)

def main():

    winHeight, winLength = 500, 400
    win = createWindow(winHeight, winLength)

    animateFace(win, winHeight, winLength)

    message = Text(Point(winLength/2, winHeight*0.05) \
                   , "Click anywhere to quit.")
    message.draw(win)
    win.getMouse()
    win.close()

main()