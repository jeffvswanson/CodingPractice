# face.py
from graphics import *

class Face:

    def __init__(self, window, center, size):
        eyeSize = 0.15 * size
        eyeOff = size / 3.0
        mouthSize = 0.8 * size
        mouthOff = size / 2.0
        self.head = Circle(center, size)
        self.head.draw(window)
        self.leftEye = Circle(center, eyeSize)
        self.leftEye.move(-eyeOff, -eyeOff)
        self.rightEye = Circle(center, eyeSize)
        self.rightEye.move(eyeOff, -eyeOff)
        self.leftEye.draw(window)
        self.rightEye.draw(window)
        p1 = center.clone()
        p1.move(-mouthSize/2, mouthOff)
        p2 = center.clone()
        p2.move(mouthSize/2, mouthOff)
        self.mouth = Line(p1, p2)
        self.mouth.draw(window)

    def smile(self, window, center, size):
        """Draws a smiling face."""
        self.head.draw(window)
        self.rightEye.draw(window)
        self.leftEye.draw(window)
        mouthSize = 0.8 * size
        mouthOff = size / 4.0
        # Left point of smile
        p1 = center.clone()
        p1.move(-mouthSize/2, mouthOff)
        # Right point of smile
        p2 = center.clone()
        p2.move(mouthSize/2, mouthOff)
        # Bottom point of smile
        p3 = center.clone()
        p3.move(0, mouthSize)
        # Define smile
        self.mouth = Polygon(p1, p2, p3)
        self.mouth.draw(window)

    def wink(self, window, center, size):
        """Draws a winking smiley face."""
        self.head.draw(window)
        self.leftEye.draw(window)
        # Set the conditions for the winking right eye.
        eyeSize = 0.25 * size
        eyeOff = size / 3.0
        eyeStart = Point(center.getX()-eyeSize/2.0,center.getY())
        self.rightEye = Line(eyeStart, Point(eyeStart.getX()+eyeSize, eyeStart.getY()))
        self.rightEye.move(eyeOff, -eyeOff)
        self.rightEye.draw(window)
        mouthSize = 0.8 * size
        mouthOff = size / 4.0
        # Left point of smile
        p1 = center.clone()
        p1.move(-mouthSize/2, mouthOff)
        # Right point of smile
        p2 = center.clone()
        p2.move(mouthSize/2, mouthOff)
        # Bottom point of smile
        p3 = center.clone()
        p3.move(0, mouthSize)
        # Define smile
        self.mouth = Polygon(p1, p2, p3)
        self.mouth.draw(window)


    def frown(self, window, center, size):
        """Draws a frowning face."""
        self.head.draw(window)
        self.rightEye.draw(window)
        self.leftEye.draw(window)
        mouthSize = 0.8 * size
        mouthOff = size / 4.0
        # Top line of frown
        p1 = center.clone()
        p1.move(-mouthSize/2, mouthOff)
        p2 = center.clone()
        p2.move(mouthSize/2, mouthOff)
        topMouth = Line(p1, p2)
        # Left side of frown
        p3 = p1.clone()
        p3.move(-mouthSize/4, mouthOff/4)
        LFrown = Line(p1, p3)
        # Right side of frown
        p4 = p2.clone()
        p4.move(mouthSize/4, mouthOff/4)
        RFrown = Line(p2, p4)
        self.mouth = [topMouth.draw(window), LFrown.draw(window), 
        RFrown.draw(window)]

    def moveFace(self, height, length, size, dx, dy):
        """Method to move the face around a window."""
        self.head.move(dx, dy)
        self.leftEye.move(dx, dy)
        self.rightEye.move(dx, dy)
        self.mouth.move(dx, dy)