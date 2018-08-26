# file: animation.py
"""Modify the cannonball animation so that the input dialog window stays on 
screen at all times."""

from graphics import GraphWin, Text, Line, Point, update
from projectile import Projectile
from inputDialog import InputDialog
from  shotTracker import ShotTracker

def main():
    # Create animation window
    win = GraphWin("Projectile Animation", 640, 480, autoflush=False)
    win.setCoords(-10, -10, 210, 155)
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
    while True:
        choice = inputwin.interact()
        if choice == "Quit": # Loop exit
            break
        # Create a shot and track until it hits ground or leaves window
        angle, vel, height = inputwin.getValues()
        shot = ShotTracker(win, angle, vel, height)
        while 0 <= shot.getY() and -10 < shot.getX() <= 210:
            shot.update(1/50)
            update(50)
main()
