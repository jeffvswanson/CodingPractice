# winterscene.pyw
# A program which draws a winter scene.
"""Write a program that draws a winter scene with a Christmas tree
and a snowman."""

from graphics import *

def main():

    win = GraphWin()
    win.setCoords(0.0, 0.0, 10.0, 10.0)

    trunk = Rectangle(Point(1.75, 0.0), Point(2.25, 0.5))
    trunk.setOutline("brown")
    trunk.setFill("brown")
    trunk.draw(win)

    bottomtreesection = Polygon(Point(1.0, 0.5), Point(3.0, 0.5), Point(2.0, 1.5))
    bottomtreesection.setOutline("green")
    bottomtreesection.setFill("green")
    bottomtreesection.draw(win)

    middletreesection = bottomtreesection.clone()
    middletreesection.move(0, 0.75)
    middletreesection.draw(win)

    toptreesection = bottomtreesection.clone()
    toptreesection.move(0, 1.5)
    toptreesection.draw(win)

    snowmanbottom = Circle(Point(6, 1), 1)
    snowmanbottom.setOutline("white")
    snowmanbottom.setFill("white")
    snowmanbottom.draw(win)

    snowmanmiddle = Circle(Point(6, 2.75), 0.75)
    snowmanmiddle.setOutline("white")
    snowmanmiddle.setFill("white")
    snowmanmiddle.draw(win)

    snowmantop = Circle(Point(6, 4), 0.5)
    snowmantop.setOutline("white")
    snowmantop.setFill("white")
    snowmantop.draw(win)

    snowmanhatbrim = Line(Point(5.5, 4.5), Point(6.5, 4.5))
    snowmanhatbrim.setOutline("black")
    snowmanhatbrim.draw(win)

    stovepipehat = Rectangle(Point(5.75, 4.51), Point(6.25, 5))
    stovepipehat.setOutline("black")
    stovepipehat.setFill("black")
    stovepipehat.draw(win)

main()
