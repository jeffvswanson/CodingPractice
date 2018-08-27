# shotTracker.py
""" Provides a class for tracking a projectile in a graphics window"""

from graphics import Circle, Point
from projectile import Projectile

class ShotTracker:

    def __init__(self, win, angle, velocity, height):
        """win is the GraphWin to display the shot. angle, velocity,
            and height are initial projectile parameters.
        """

        self.proj = Projectile(angle, velocity, height)
        self.marker = Circle(Point(0, height), 3)
        self.marker.setFill("red")
        self.marker.setOutline("red")
        self.marker.draw(win)

    def update(self, dt):
        """Move the shot dt seconds farther along its flight """

        # Update the projectile
        self.proj.update(dt)

        # Moves the circle to the new projectile location
        center = self.marker.getCenter()
        dx = self.proj.getX() - center.getX()
        dy = self.proj.getY() - center.getY()
        self.marker.move(dx, dy)

    def getX(self):
        """ return the current x coordinate of the shot's center """
        return self.proj.getX()

    def getY(self):
        """ return the current y coordinate of the  shot's center """
        return self.proj.getY()

    def undraw(self):
        """ undraw the shot """
        self.marker.undraw()