# regressionClass.py

"""regressionClass.py
Provides a class to support linear
regression modeling."""

from graphics import *

class Regression:

    """All the tools needed to draw a line of regression."""

    def __init__(self, win):
        """Creates the line of regression object do which points can be added."""
        self.win = win
        self.pointsList = []
        self.sumX, self.sumY = 0, 0
        self.sumXSquared = 0
        self.sumXY = 0

    def addPoint(self, point):
        """Adds a point to the line of regression."""
        self.pointsList.append(point)

    def predict(self, x):
        """Accepts a value of x as a parameter, and returns the value of the 
        corresponding y on the line of best fit."""
        b = self.rPoint.getY() - self.lineSlope * self.rPoint.getX()
        y = self.lineSlope * x + b
        print("The y-value at {0} is {1}".format(x, y))

    def drawLine(self, xL, xR):
        """Draws the regression line"""
        self.rPoint, self.lPoint, self.lineSlope = self.__calcRegressionLineEndPoints(self.pointsList, xL, xR)

        self.lineOfRegression = Line(self.rPoint, self.lPoint)
        self.lineOfRegression.setOutline("Orange")
        self.lineOfRegression.draw(self.win)
 
    def __calcRegressionLineEndPoints(self, pointsList, xL, xR):
        """Internal function to calculate the regression line endpoints."""
        n = len(pointsList)
        for pt in pointsList:
            self.sumX = self.sumX + pt.getX()
            self.sumY = self.sumY + pt.getY()
            self.sumXSquared = self.sumXSquared + (pt.getX()) ** 2
            self.sumXY = self.sumXY + (pt.getX() * pt.getY())

        avgX = self.sumX / n
        avgY = self.sumY / n
        lineSlope = (self.sumXY - n * avgX * avgY)/(self.sumXSquared - n * avgX ** 2)

        y1 = avgY + lineSlope * (xL - avgX)
        y2 = avgY + lineSlope * (xR - avgX)

        rPoint = Point(xL, y1)
        lPoint = Point(xR, y2)

        return rPoint, lPoint, lineSlope
        