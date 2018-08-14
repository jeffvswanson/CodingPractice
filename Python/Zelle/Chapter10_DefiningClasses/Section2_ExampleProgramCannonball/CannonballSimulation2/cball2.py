# cball2.py
# A program to calculate the distance a projectile travels in the x-direction.

from math import pi, sin, cos, radians

def getInputs():
    angle = float(input("Enter the launch angle (in degrees): "))
    vel = float(input("Enter the initial velocity (in meters/sec): "))
    h0 = float(input("Enter the initial height (in meters): "))
    time = float(input(
        "Enter the time interval between position calculations: "))
    return angle, vel, h0, time


def getXYComponents(vel, angle):
    # convert the angle from degrees to radians
    theta = radians(angle)

    # set the initial position and velocities in the x- and y-directions.
    xvel = vel * cos(theta)
    yvel = vel * sin(theta)
    return xvel, yvel

def updateCannonBall(time, xpos, ypos, xvel, yvel):
    xpos = xpos + time * xvel
    yvel1 = yvel - time * 9.8
    ypos = ypos + time * (yvel + yvel1)/2.0
    yvel = yvel1
    return xpos, ypos, yvel

def main():
    angle, vel, h0, time = getInputs()
    xpos, ypos = 0, h0
    xvel, yvel = getXYComponents(vel, angle)
    while ypos >= 0:
        xpos, ypos, yvel = updateCannonBall(time, xpos, ypos, xvel, yvel)
    print("\nDistance traveled: {0:0.1f} meters.".format(xpos))
main()



