# cannonballMaxHeight.py
"""Modify the cannonball simulation from the chapter so that it also calculates
the maximum height achieved by the cannonball."""

from projectile import Projectile

def getInputs():
    while True:
        try:
            a = float(input("Enter the launch angle (in degrees): "))
        except (SyntaxError, NameError, TypeError, ValueError):
            print("You have to enter a positive number.")
            continue
        if a <= 0:
            print("You have to enter a positive number.")
            continue
        else:
            break
    while True:
        try:
            v = float(input("Enter the initial velocity (in meters/sec): "))
        except (SyntaxError, NameError, TypeError, ValueError):
            print("You have to enter a positive number.")
            continue
        if v <= 0:
            print("You have to enter a positive number.")
            continue
        else:
            break
    while True:
        try:
            h = float(input("Enter the initial height (in meters): "))
        except (SyntaxError, NameError, TypeError, ValueError):
            print("You have to enter a positive number.")
            continue
        if h <= 0:
            print("You have to enter a positive number.")
            continue
        else:
            break
    while True:
        try:
            t = float(input(
                "Enter the time interval between position calculations: "))
        except (SyntaxError, NameError, TypeError, ValueError):
            print("You have to enter a positive number.")
            continue
        if t <= 0:
            print("You have to enter a positive number.")
            continue
        else:
            break
    return a,v,h,t

def main():
    angle, vel, h0, time = getInputs()
    cball = Projectile(angle, vel, h0)
    while cball.getY() >= 0:
        cball.update(time)
    print("\nDistance traveled: {0:0.1f} meters.".format(cball.getX()))
    print("The maximum height of the projectile was {0:0.1f} meters."
    .format(cball.getYmax()))
main()
