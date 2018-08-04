# bouncingBall.pyw
# A program which animates a bouncing ball around a window.
"""Write a program to animate a circle bouncing around a window. The basic idea
is to start the circle somewhere in the interior of the window. Use variables 
dx and dy (both initialized to 1) to control the movement of the circle. Use a
large counted loop (say 10000 iterations), and each time through the loop move 
the circle using dx and dy. When the x-value of the center of the circle get 
too high (it hits the edge), change dx to -1. When it gets too low, change dx
back to 1. Use a similar approach for dy.
    Note: Your animation will probably run too fast. You can slow it down by 
    using update from the graphics library with a rate parameters. For example,
    this loop will be limited to going around at a rate of 30 times per second:

    for i in range(10000):
        ...
        update(30) # pause so rate is not more than 30 times a second."""

from graphics import *

def createGraphics(winHeight, winLength):

    win = GraphWin("Bouncing Ball Animation",winLength, winHeight)
    win.setCoords(0.0, 0.0, winLength, winHeight)

    radius = (1/10) * winHeight
    ball = Circle(Point(winLength/2, winHeight/2), radius)
    ball.setOutline("black")
    ball.setFill("black")
    ball.draw(win)

    return win, ball, radius

def animateBall(win, ball, radius, length, height):

    animationLength = 10000
    dx = 1
    dy = 1
    ball.getCenter().getX()
    for i in range(animationLength):
        
        if (ball.getCenter().getX() + radius) + dx >= length:
            dx = -1
        elif (ball.getCenter().getX() - radius) - dx <= 0:
            dx = 1

        if (ball.getCenter().getY() + radius) + dy >= height:
            dy = -1
        elif (ball.getCenter().getY() - radius) - dy <=0:
            dy = 1

        ball.move(dx, dy)
        update(60)   

def main():

    winHeight = 500
    winLength = 400

    win, ball, radius = createGraphics(winHeight, winLength)

    animateBall(win, ball, radius, winLength, winHeight)

    message = Text(Point(winLength/2, winHeight*0.05), \
    "Click anywhere to quit.")
    message.draw(win)
    win.getMouse()
    win.close()

main()
