# file: animation.py
"""Advanced: Add a Target class to the cannonball animation. A target should be
a rectangle placed at a random x position at the bottom of the window. Allow 
users to keep firing until they hit the target."""

from graphics import GraphWin, Text, Line, Point, update
from projectile import Projectile
from inputDialog import InputDialog
from shotTracker import ShotTracker
from target import Target

def main():
    # Create animation window
    win = GraphWin("Projectile Animation", 640, 480, autoflush=False)
    width = 210
    win.setCoords(-10, -10, width, 155)
    # Draw baseline
    Line(Point(-10, 0), Point(210, 0)).draw(win)
    # Draw labeled ticks every 50 meters
    for x in range(0, 210, 50):
        Text(Point(x, -5), str(x)).draw(win)
        Line(Point(x, 0), Point(x, 2)).draw(win)
    # Event loop, each time through fires a single shot
    angle, vel, height = 45.0, 40.0, 2.0
    # Interact with the user
    inputwin = InputDialog(angle, vel, height)
    target = Target(win, width, angle, vel, height)
    p = (0, 1)
        # Loop for striking the target
    while target.hit(p) == False:
        # Loop to shoot the projectile
        while True:
            choice = inputwin.interact()
            if choice == "Quit": # Loop exit
                break
            # Create a shot and track until it hits target or leaves window
            angle, vel, height = inputwin.getValues()
            shot = ShotTracker(win, angle, vel, height)
            while (0 <= shot.getY() and -10 < shot.getX() <= 210) \
            or target.hit(p):
                if target.hit(p) == True:
                    break
                shot.update(1/50)
                update(50)
main()
### Figure out how to break out of the nested while loop as it 
### makes the overall loop infinite