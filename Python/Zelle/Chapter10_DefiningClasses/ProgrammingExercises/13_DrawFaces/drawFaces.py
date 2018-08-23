# drawFace.py
# A program to draw a face from the face class in face.py
"""See face.py for class definition. Add methods to this class that cause the 
face to change expression. For example, you might add methods such as smile, 
wink, frown, flinch, etc. Your class should implement at least three such
methods.
    Use your class to write a program that draws a face and provides the user
with the buttons to change the facial expression."""

from graphics import *

from button import Button
from face import Face

def createWindow():
    win = GraphWin("Face Drawing", 400, 400)
    xCenter = 200
    yCenter = 199
    center = Point(xCenter, yCenter)
    size = 100
    Text(Point(xCenter, 25), \
    "Press a button to change the face.").draw(win)
    return win, center, size

def makeButtons(win):
    grimButton = Button(win, Point(75, 75), 100, 25, "Grim Face")
    grimButton.activate()
    smileButton = Button(win, Point(75, 375), 100, 25, "Smiley Face")
    smileButton.activate()
    quitButton = Button(win, Point(200, 375), 75, 25, "Quit")
    quitButton.activate()
    winkButton = Button(win, Point(300, 75), 100, 25, "Winking Face")
    winkButton.activate()
    frownButton = Button(win, Point(300, 375), 100, 25, "Frowney Face")
    frownButton.activate()
    return grimButton, smileButton, winkButton, frownButton, quitButton

def cleanSlate(win, center, size):
    # Function to cover up the face
    coverUp = Circle(center, size)
    coverUp.setFill("light gray")
    coverUp.draw(win)

def changeFaces(win, center, size):
    # Need to figure out a way to get the window to undraw the face before drawing
    # the next face, otherwise I get an error
    grimButton, smileButton, winkButton, frownButton, quitButton = \
    makeButtons(win)
    theFace = Face(win, center, size)
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if grimButton.clicked(pt):
            cleanSlate(win, center, size)
            theFace = Face(win, center, size)
        elif smileButton.clicked(pt):
            cleanSlate(win, center, size)
            theFace.smile(win, center, size)
        elif winkButton.clicked(pt):
            cleanSlate(win, center, size)
            theFace.smile(win, center, size)
        elif frownButton.clicked(pt):
            cleanSlate(win, center, size)
            theFace.frown(win, center, size)
        else:
            pass

def main():

    win, center, size = createWindow()

    changeFaces(win, center, size)


main()
