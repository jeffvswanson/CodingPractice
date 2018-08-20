# sphereClass.py
"""Module representing the class Sphere."""

import math

class Sphere:
    """A sphere object. The radius is returned with getRadius(),
    the sphere's surface area is calculated with surfaceArea(),
    and the volume with volume()."""

    def __init__(self, radius):
        """Creates a sphere of a given radius."""
        self.radius = float(radius)

    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        area = 4 * math.pi * self.radius ** 2
        return area

    def volume(self):
        v = (4/3) * math.pi * self.radius ** 3
        return v
