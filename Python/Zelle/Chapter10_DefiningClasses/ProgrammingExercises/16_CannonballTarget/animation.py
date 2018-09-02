# file: animation.py
"""Advanced: Add a Target class to the cannonball animation. A target should be
a rectangle placed at a random x position at the bottom of the window. Allow 
users to keep firing until they hit the target."""

from graphics import GraphWin, Text, Line, Point, update
from button import Button
from projectile import Projectile
from inputDialog import InputDialog
from shotTracker import ShotTracker
from target import Target

def Introduction():
    # Introduction and explain the rules
    win = GraphWin("Target Practice")
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")
    readButton = Button(win, Point(5, 1), 6, 1, "I read the rules")
    readButton.activate()
    rulesBox = Button(win, Point(5, 6), 9, 7, 
"""You have to hit 
the blue target 
with the red ball. 
The program keeps 
looping until you 
hit the target or 
choose to quit.""")
    rulesBox.activate()

    # Only move on to the game after the rules have been read
    pt = win.getMouse()
    while not readButton.clicked(pt):
        pt = win.getMouse()
    win.close()

def createGameWindow():
    win = GraphWin("Projectile Animation", 640, 480, autoflush=False)
    width = 210
    win.setCoords(-10, -10, width, 155)
    # Draw baseline
    Line(Point(-10, 0), Point(210, 0)).draw(win)
    # Draw labeled ticks every 50 meters
    for x in range(0, 210, 50):
        Text(Point(x, -5), str(x)).draw(win)
        Line(Point(x, 0), Point(x, 2)).draw(win)
    return win, width

def playTheGame(win, width):
    # Event loop, each time through fires a single shot
    angle, vel, height = 45.0, 40.0, 2.0
    # Interact with the user
    inputwin = InputDialog(angle, vel, height)
    target = Target(win, width, angle, vel, height)
    p = Point(100, 20)
        # Loop for striking the target
    while not(target.hit(p)):
        # Loop to shoot the projectile
        choice = inputwin.interact()
        if choice == "Quit":
            inputwin.close()
            return choice
        # Create a shot and track until it hits target or leaves window
        angle, vel, height = inputwin.getValues()
        shot = ShotTracker(win, angle, vel, height)
        p = checkForHit(shot, target)
        print("hitTarget=", target.hit(p))
    inputwin.close()
    return target.hit(p)

def checkForHit(shot, target):
    p = Point(shot.getX(), shot.getY())
    while (0 <= shot.getY() and -10 < shot.getX() <= 210) \
    and not(target.hit(p)):
        shot.update(1/50)
        update(50)
        p = Point(shot.getX(), shot.getY())
    return p

def Outro(win, result):
    outroWin = GraphWin("Target Practice Result")
    outroWin.setCoords(0, 0, 10, 10)
    resultsButton = Button(outroWin, Point(5, 1), 6, 1, "I read the results")
    resultsButton.activate()
    if result == True:
        resultsBox = Button(outroWin, Point(5, 6), 9, 7, 
        """You hit the target!""")
    else:
        resultsBox = Button(outroWin, Point(5, 6), 9, 7,
        """You pressed the quit button.""")
    resultsBox.activate()
    # Only move on to the game after the results have been read
    pt = outroWin.getMouse()
    while not resultsButton.clicked(pt):
        pt = outroWin.getMouse()
    win.close()
    outroWin.close()

def main():
    Introduction()
    # Create animation window
    win, width = createGameWindow()
    # Go play target practice
    result = playTheGame(win, width)
    Outro(win, result)
main()
### Figure out how to break out of the nested while loop as it 
### makes the overall loop infinite

## I want to add an introduction explaining the goal of the program

## Probably have to do something with getting the ShotTracker to return the center