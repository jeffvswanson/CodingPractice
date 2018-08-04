# face.pyw
# A program which draws a face.
"""Write a program that draws some sort of face."""

from graphics import *

def main():

    win = GraphWin()
    win.setCoords(0.0, 0.0, 10.0, 10.0)

    head = Circle(Point(5, 5), 4)
    head.setOutline("peachpuff")
    head.setFill("peachpuff")
    head.draw(win)

    leftEye = Circle(Point(3, 6.5), 1)
    leftEye.setOutline("black")
    leftEye.setFill("black")
    leftEye.draw(win)

    rightEye = leftEye.clone()
    rightEye.move(4, 0)
    rightEye.draw(win)

    upperNose = Line(Point(4.5, 6), Point(3.5, 5))
    upperNose.draw(win)

    lowerNose = Line(Point(3.5, 5), Point(4.5, 4))
    lowerNose.draw(win)

    mouth = leftEye.clone()
    mouth.move(2, -4)
    mouth.draw(win)
    
main()
