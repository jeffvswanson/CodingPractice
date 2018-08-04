# photoAnonymizer.pyw
"""Use your drawFace function form the previous exercise to wite a photo
anonymizer. this program allows a user to load an image file (such as a PPM or
GIF) and to draw cartoon faces over the top of existing faces in the photo. The
user first inputs the name of the file containing the image. The image is
displayed and the user is asked how many faces are to be blocked. The program
then enters a loop for the user to click on two points for each face: the center
and somewhere on the edge of the face (to determine the size of the face.) The
program should then draw a face in that location using the drawFace function.

Hints: Section 4.8.4 describes the image-manipulation methods in the graphics
library. Display the image centered in a GraphWin that is the same width and
height as the image, and draw the graphics into this window. You can use a
screen capture utility to save the resulting images."""

import math
from graphics import *

def getInfo():
    win = GraphWin("Input File Name", 400, 400)
    win.setBackground("white")
    win.setCoords(0.0, 0.0, 4.0, 4.0)
    message = Text(Point(2.0, 3.5), """This program allows you to anonymize
by clicking on the center of a face
and the edge of the face to draw a
cartoon face.""").draw(win)
    Text(Point(0.75, 2.5), "Input file name: ").draw(win)
    infileEntry = Entry(Point(2.25, 2.5), 20)
    infileEntry.setText("")
    infileEntry.draw(win)

    button = Text(Point(2, 1.5), "Get the file!")
    button.draw(win)
    Rectangle(Point(1, 1.0), Point(3, 2)).draw(win)

    win.getMouse()
    win.close()

    # Get the image height and width in pixels and center it.
    photo = Image(Point(0, 0), infileEntry.getText())
    w = photo.getWidth()
    h = photo.getHeight()
    photo.move(w/2, h/2)

    return photo, w, h

def getNumFaces():
    win = GraphWin("Input Number of faces", 400, 400)
    win.setBackground("white")
    win.setCoords(0.0, 0.0, 4.0, 4.0)
    Text(Point(2, 3), "How many faces are there? ").draw(win)
    faceEntry = Entry(Point(2, 2.75), 20)
    faceEntry.setText("0")
    faceEntry.draw(win)
    
    button = Text(Point(2, 1.5), "Let's anonymize!")
    button.draw(win)
    Rectangle(Point(1, 1.0), Point(3, 2)).draw(win)
    win.getMouse()
    win.close()
    
    count = int(faceEntry.getText())
    
    return count

def drawFace(center, size, win):
    x = center.getX()
    y = center.getY()
    head = Circle(Point(x, y), size)
    head.setOutline("peachpuff")
    head.setFill("peachpuff")
    head.draw(win)

    leftEye = Circle(Point((x - (1/2) * size), (y + (1/2) * size))\
                     , (size/10))
    leftEye.setOutline("black")
    leftEye.setFill("black")
    leftEye.draw(win)

    rightEye = leftEye.clone()
    rightEye.move(size, 0)
    rightEye.draw(win)

    #upperNose = Line(Point(4.5, 6), Point(3.5, 5))
    upperNose = Line(Point(x - 1/10 * size, y + size * (1/3)),\
                     Point(x - (1/2) * size, y))
    upperNose.draw(win)

    #lowerNose = Line(Point(3.5, 5), Point(4.5, 4))
    lowerNose = Line(Point(x - (1/2) * size, y)\
                     , Point(x - 1/10 * size, y - size * (1/3)))
    lowerNose.draw(win)

    mouth = leftEye.clone()
    mouth.move(1/2 * size, -size)
    mouth.draw(win)

    return

def main():

    # Get the photo information
    photo, width, height = getInfo()

    # Draw the photo
    win = GraphWin("Photo Anonymizer", width, height)
    photo.draw(win)

    # Get the number of faces
    count = getNumFaces()

    for i in range(count):
        message = Text(Point(width/2, height - (height - height/20)),
             "Click on the center of the face, then the edge").draw(win)
        center = win.getMouse()
        edge = win.getMouse()
        size = math.sqrt((center.getX() - edge.getX())**2 \
                         + (center.getY() - edge.getY())**2)
        drawFace(center, size, win)

    message.setText("Click to exit")
    message.setTextColor("pink")
    message.setStyle("bold")
    message.setSize(18)
    win.getMouse()
    win.close()

main()


    
