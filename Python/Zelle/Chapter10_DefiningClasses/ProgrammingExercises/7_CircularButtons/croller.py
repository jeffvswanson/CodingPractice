# croller.py
# Graphics program to roll a pair of dice. Uses custom widget CButton and 
# DieView
"""Write a modified Button class that creates circular buttons. Call your class
CButton and implement the exact rame methods that are in the existing Button 
class. Your constructor should take the center of the button and its radius as
normal parameters. Place your class in a module called cbutton.py. Test your 
class by modifying roller.py to use your buttons."""

from random import randrange
from graphics import GraphWin, Point

from cbutton import CButton
from dieview import DieView

def main():

    # create the application window
    win = GraphWin("Dice Roller")
    win.setCoords(0,0, 10, 10)
    win.setBackground("green2")

    # Draw the interface widgets
    die1 = DieView(win, Point(3, 7), 2)
    die2 = DieView(win, Point(7, 7), 2)
    rollButton = CButton(win, Point(5, 4), 1.75, "Roll Dice")
    rollButton.activate()
    quitButton = CButton(win, Point(5, 1), 1, "Quit")

    # Event loop
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            value1 = randrange(1, 7)
            die1.setValue(value1)
            value2 = randrange(1, 7)
            die2.setValue(value2)
            quitButton.activate()
        pt = win.getMouse()

    # close up shop
    win.close()
    
main()
