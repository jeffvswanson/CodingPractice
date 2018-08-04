# triangle3.pyw
"""Write a function that computes the area of a triangle given the length of its
three sides as parameters (see Programming Exercise 9 from Chapter 3). Use your
function to augment triangle2.py from this chapter so that it also displays the
area of the triangle."""

from graphics import *
import math

def square(x):
    return x * x

def distance(p1, p2):
    dist = math.sqrt(square(p2.getX() - p1.getX())
                     + square(p2.getY() - p1.getY()))
    return dist
    
def triangleArea(perim, a, b, c):
    p = perim/2
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return area

def main():

    win = GraphWin("Draw a Triangle", 400, 400)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points.")
    message.draw(win)

    # Get and draw three vertices of a triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # Use Polygon object to draw the triangle
    triangle = Polygon(p1, p2, p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    # Calculate the perimeter of the triangle
    a = distance(p1, p2)
    b = distance(p2, p3)
    c = distance(p3, p1)
    perim = a + b + c
    message.setText("The perimeter is: {0:0.2f} units.".format(perim))
    win.getMouse()

    #Calculate the area of a triangle
    area = triangleArea(perim, a, b, c)
    message.setText("The area is: {0:0.2f} square units".format(area))
    win.getMouse()

    # Wait for another click to exit
    message.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()

main()
