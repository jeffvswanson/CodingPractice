# regressionClass.py

"""regressionClass.py
Provides a class to support linear
regression modelling."""

from graphics import *

class Regression:

    """All the tools needed to draw a line of regression."""

    def __init__(self, win):
        """Creates the line of regression object do which points can be added."""
        self.win = win
        self.pointsList = []
        self.rPoint, self.lPoint = 
            __calcRegressionLineEndPoints(self.pointsList)

        self.lineOfRegression = Line(self.rPoint, self.lPoint)
        self.lineOfRegression.setOutline("Orange")
        self.lineOfRegression.draw(win)

    def addPoint(self, point):
        """Adds a point to the line of regression."""
        self.pointsList.append(point)

    def predict(self):
        """Accepts a value of x as a parameter, and returns the value of the 
        corresponding y on the line of best fit."""

    def __calcRegressionLineEndPoints(self, pointsList):
        """Internal function to calculate the regression line slope."""
        n = len(self.pointsList)
        for pt in self.pointsList:
            sumX = sumX + pt.getX()
            sumY = sumY + pt.getY()
            sumXSquared = sumXSquared + (pt.getX()) ** 2
            sumXY = sumXY + (pt.getX() * pt.getY())

        avgX = sumX / n
        avgY = sumY / n
        lineSlope = (sumXY - n * avgX * avgY)/(sumXSquared - n * avgX ** 2)

        # Set the left and right limits according to the coordinate system
        x1 = 5
        x2 = 45

        y1 = avgY + lineSlope * (x1 - avgX)
        y2 = avgY + lineSlope * (x2 - avgX)

        rPoint = Point(x1, y1)
        lPoint = Point(x2, y2)

        return rPoint, lPoint
        