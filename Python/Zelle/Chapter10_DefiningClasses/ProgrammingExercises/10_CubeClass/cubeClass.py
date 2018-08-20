# cubeClass.py
"""Module representing the class Cube."""

class Cube:
    """A cube object. The length of an edge is returned with getEdge(),
    the cube's surface area is calculated with surfaceArea(), and
    the volume with volume()."""

    def __init__(self, edge):
        """Creates a cube with a given edge length."""
        self.edge = float(edge)

    def getEdge(self):
        return self.edge

    def surfaceArea(self):
        area = 6 * (4 * self.edge)
        return area

    def volume(self):
        v = self.edge ** 3
        return v
