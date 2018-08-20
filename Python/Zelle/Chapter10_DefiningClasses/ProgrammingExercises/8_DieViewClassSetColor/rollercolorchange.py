# rollerColorChange.py
# Graphics program to roll a pair of dice which changes
# the color of the pips randomly. Uses custom widget
# Button and DieView
"""Modify the DieView class from the chapter by adding a method that allows the
color of the pips to be specified.
    setColor(self, color) Changes the color of the pips to color.
Hints: You can change the color by changing the value of the instance variable
foreground, but you also need to redraw the die after doing this. Modify 
setValue so that it remembers the value of the die in an instance variable.
Then setColor can call setValue andpass the stored value to redraw the die. You
can test your new class with the roller.py program. Have the dice change to a 
random color after each roll (you can generate a random color with the 
color_rgb function)."""

from random import randrange
from graphics import GraphWin, Point, color_rgb

from button import Button
from dieview import DieView

def randColor():
    r = randrange(0, 255)
    g = randrange(0, 255)
    b = randrange(0, 255)
    color = color_rgb(r, g, b)
    return color

def main():

    # create the application window
    win = GraphWin("Dice Roller")
    win.setCoords(0,0, 10, 10)
    win.setBackground("green2")

    # Draw the interface widgets
    die1 = DieView(win, Point(3, 7), 2)
    die2 = DieView(win, Point(7, 7), 2)
    rollButton = Button(win, Point(5, 4.5), 6, 1, "Roll Dice")
    rollButton.activate()
    quitButton = Button(win, Point(5, 1), 2, 1, "Quit")

    # Event loop
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            color = randColor()
            value1 = randrange(1, 7)
            die1.setValue(value1)
            die1.setColor(color)
            value2 = randrange(1, 7)
            die2.setValue(value2)
            die2.setColor(color)
            quitButton.activate()
            
        pt = win.getMouse()

    # close up shop
    win.close()
    
main()
