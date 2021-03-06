# target.py
from random import randrange

from graphics import *
from projectile import Projectile
from shotTracker import ShotTracker


class Target:

    """A target used in conjuction with animation.py. The hit(p) method returns
    true if the target is hit with the projectile."""

    def __init__(self, window, width, angle, velocity, height):
        """Creates a rectangular target placed at a random x position at the 
        bottom of a window."""
        
        self.proj = Projectile(angle, velocity, height)
        # Create the width of the rectangle base off the size of the window
        w = width/10
        # Use randrange to get the left edge of the rectangle
        # Make sure the target does not go off the screen
        self.xL = randrange(0, (width - w))
        # Define right edge of the rectangle
        self.xR = self.xL + w
        # Define y-values
        self.yL = 0
        self.yR = 5
        # Define the target rectangle
        self.Target = Rectangle(Point(self.xL, self.yL), \
        Point(self.xR, self.yR))
        self.Target.setFill("blue")
        self.Target.draw(window)

    def hit(self, p):
        "Returns true if the projectile strikes the target"
        # Account for the edges of the projectile.
        return ((self.xL <= p.getX() + 3) and \
        ((p.getX() - 3) <= self.xR)) and \
        (p.getY() <= self.yR)
