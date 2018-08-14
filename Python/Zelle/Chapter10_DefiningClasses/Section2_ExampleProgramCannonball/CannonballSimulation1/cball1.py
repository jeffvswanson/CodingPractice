# cball1.py
# A program to calculate the distance a projectile travels in the x-direction.

from math import pi, sin, cos, radians

def main():
    angle = float(input("Enter the launch angle (in degrees): "))
    vel = float(input("Enter the initial velocity (in meters/sec): "))
    h0 = float(input("Enter the initial height (in meters): "))
    time = float(input(
        "Enter the time interval between position calculations: "))

    xpos = 0.0
    ypos = h0

    # convert the angle from degrees to radians
    theta = radians(angle)

    # set the initial position and velocities in the x- and y-directions.
    xvel = vel * cos(theta)
    yvel = vel * sin(theta)
    
    # loop until the ball hits the ground
    while ypos >= 0.0:
        xpos = xpos + time * xvel
        yvel1 = yvel - time * 9.8
        ypos = ypos + time * (yvel + yvel1)/2.0
        yvel = yvel1

    print("\nDistance traveled: {0:0.1f} meters.".format(xpos))
main()
