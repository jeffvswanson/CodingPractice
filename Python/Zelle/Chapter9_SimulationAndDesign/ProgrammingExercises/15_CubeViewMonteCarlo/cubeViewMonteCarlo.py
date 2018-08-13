# cubeViewMonteCarlo.py
# A program that estimates how much of a cube wall you can see using a Monte 
# Carlo simulation.
"""(Advanced) Here ir a puzzle problem that can be solved with either some 
fancy analytic geometry (calculus) or a relatively simple simulation.
    Suppose you are located at the exact center of a cube. If you could look
all around you in every direction, each wall of the cube would occupy 1/6 of 
your wield of vision. Suppose you move toward one of the walls so that you are
now halfway between it and the center of the cube. What fraction of your field
of vision is now taken up by the closest wall? Hint: Use a Monte Carlo 
simulation that repeatedly "looks" in a random direction and counts how many 
times it sees the wall."""

from random import choice, uniform

def main():

    printIntro()
    # Find out how many times the user wants to "look"
    n = getInput()
    # Find the number of times a glance looks at the closest wall.
    # fov is short for field of view
    fov = sim(n)
    printSummary(n, fov)

def printIntro():
    print("This program estimates how much of your field of view a cube wall \
would take up if you were halfway between the wall and the center of the cube \
using a Monte Carlo simulation.")

def getInput():
    n = 0
    while n < 1:
        try:
            n = int(input("Please enter the number of glances you want to take \
in random directions within the cube: "))
        except (SyntaxError, NameError, TypeError, ValueError):
            print("You have to enter a whole number.")
            continue
        if n < 1:
            print("You have to simulate at least one glance.")
            continue
    return n

def sim(n):
    # Design a cube, the size doesn't matter, using size of 1
    # Have the user look randomly around the cube from the point (0.5, 0, 0)
    # The user is looking at a specific wall or its opposite wall
    wall = [-1, 1]
    # Only accumulate values that hit within the closest cube wall
    fov = 0
    for i in range(n):
        # Start with deciding if the x-direction glance is looking on the half
        # of the cube with the closest wall, then randomize the y and z 
        # coords.
        # glanceDir is the direction the random glance looks
        # Treat the y and z fields of view as right triangles with a height 
        # of 1 and a base of 0.5.
        # arctan(0.5/1) = 26.5 degrees times 2 for the entire face is 53.
        # Therefore, if a glance is between -53 and 53 degrees in the y and z
        # direction the glance has the closest wall in its view.
        glanceDirX = choice(wall)
        glanceDirY = uniform(-90, 90)
        glanceDirZ = uniform(-90, 90)
        # Accumulate fov after taking out all glances that do not include the
        # wall we're interested in.
        if not(glanceDirX == -1 and (glanceDirY >= -53 and glanceDirY <= 53) \
        or (glanceDirZ >= -53 and glanceDirZ <= 53)):
            fov = fov + 1
    return fov

def printSummary(n, fov):
    print("After taking {0} random glances around the cube, the closest cube \
wall takes up {1:0.1%} of your field of view.".format(n, fov/n))

if __name__ == '__main__': main()