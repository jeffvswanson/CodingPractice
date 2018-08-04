# drawFace.pyw
# A program which draws faces
"""Write and test a function to meet this specification.

drawFace(center, size, win) center is a Point, size is an int, and win is a
GraphWin. Draws a simple face of the given size in win.

Your function can draw a simple smiley (or grim) face. Demonstrate the function
by writing a program that draws several faces of varying size in a single
window."""

from graphics import *

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

def properties(win):
    # Get where the user wants to center the face
    print("\nPlease click where the center of the face should be.")
    center = win.getMouse()    

    # Get the size of the face you want to draw
    sizeFace = float(input("\nPlease enter the size of the face you want \
to draw. "))

    return center, sizeFace

def main():

    # Get the dimensions of the window
    winHeight = float(input("Please enter the height of the window you want: "))
    winWidth = float(input("Please enter the  width of the window you want: "))
    win = GraphWin("Draw a Face", winHeight, winWidth)

    center, size = properties(win)

    drawFace(center, size, win)

    center, size = properties(win)

    drawFace(center, size, win)

    message = Text(Point(winWidth/2, winHeight - (winHeight - winHeight/20))\
                   , "Click anywhere to quit.")
    message.draw(win)
    win.getMouse()
    win.close()
        
main()
