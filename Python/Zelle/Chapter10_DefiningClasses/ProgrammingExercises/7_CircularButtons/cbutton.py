# cbutton.py
"""Module to make circular buttons."""
from graphics import *

class CButton:

    """A circular button is a labeled circle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, radius, label):
        """Creates a circular button, eg:
        qb = CButton(myWin, centerPoint, radius, 'Quit') """

        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+radius, x-radius
        self.ymax, self.ymin = y+radius, y-radius
        self.circ = Circle(center, radius)
        self.circ.setFill('lightgray')
        self.circ.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        "Returns true if button active and p is inside."
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.circ.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.circ.setWidth(1)
        self.active = False
