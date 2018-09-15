# projectileApp.py

from graphics import *
from launcher import Launcher

class ProjectileApp:

    def __init__(self):
        # Create graphics window with a scale line at the bottom
        self.win = GraphWin("Projectile Animation", 640, 480)
        self.win.setCoords(-10, -10, 210, 155)
        Line(Point(-10, 0), Point(210, 0)).draw(self.win)
        for x in range(0, 210, 50):
            Text(Point(x, -7), str(x)).draw(self.win)
            Line(Point(x, 0), Point(x, 2)).draw(self.win)

        # Add the launcher to the window
        self.launcher = Launcher(self.win)

        # Starts with an empty list of live shots
        self.shots = []

    def run(self):
    
        # Main event/animation loop
        while True:
            self.updateShots(1/30)

            key = self.win.checkKey()
            if key in ["q", "Q"]:
                break
            
            if key == "Up":
                self.launcher.adjAngle(5)
            elif key == "Down":
                self.launcher.adjAngle(-5)
            elif key == "Right":
                self.launcher.adjVel(5)
            elif key == "Left":
                self.launcher.adjVel(-5)
            elif key in ["f", "F"]:
                self.shots.append(launcher.fire())

            update(30)
        
        win.close()

    def updateShots(self, dt):
        alive = []
        for shot in self.shots:
            shot.update(dt)
            if shot.getY() >= 0 and -10 < shot.getX() < 210:
                alive.append(shot)
            else:
                shot.undraw()
        self.shots = alive

if __name__ == "__main__":
    ProjectileApp().run()