# threeButtonMonte.py
# Graphics program to guess which door is the correct one out of three.
"""Write a program to play "Three Button Monte." Your program should draw three
buttons labeled "Door 1," "Door 2," and "Door 3" in a window and randomly 
select one of the buttons (without telling the user which one is selected). The
program then prompts the user to click on one of the buttons. A click on the 
special button is a win, and a click on one of the other two is a loss. You
should tell the user whether they won or lost, and in the case of a loss, which
was the correct button. Your program should be entirely graphical; that is, all
prompts and messages should be displayed in the graphics window."""

from random import randrange
from graphics import *

from button import Button

def Introduction():
    # Introduction and explain the rules
    win = GraphWin("Three Button Monte")
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")
    readButton = Button(win, Point(5, 1), 6, 1, "I read the rules")
    readButton.activate()
    rulesBox = Button(win, Point(5, 6), 9, 7, """One door is the winner.
You have to pick it.""")
    rulesBox.activate()

    # Only move on to the game after the rules have been read
    pt = win.getMouse()
    while not readButton.clicked(pt):
        pt = win.getMouse()
    win.close()

def createGameWindow():
    # Create the game window for the doors
    win = GraphWin("Three Button Monte")
    win.setCoords(0, 0, 100, 50)
    win.setBackground("green2")

    # Draw the interface widgets
    door1 = Button(win, Point(20, 35), 25, 25, "Door 1")
    door2 = Button(win, Point(50, 35), 25, 25, "Door 2")
    door3 = Button(win, Point(80, 35), 25, 25, "Door 3")

    shuffleButton = Button(win, Point(50, 17.5), 50, 5, "Shuffle Doors")
    shuffleButton.activate()

    resultButton = Button(win, Point(50, 7.5), 80, 10, "Result")
    resultButton.deactivate()

    return win, door1, door2, door3, shuffleButton, resultButton

def playTheGame(win, door1, door2, door3, shuffleButton, resultButton):
    # Have the user shuffle the winning door
    pt = win.getMouse()
    winningDoor = randrange(1,4)
    while not shuffleButton.clicked(pt):
        pt = win.getMouse()        

    # Deactivate the shuffleButton and activate the doors
    shuffleButton.deactivate()
    door1.activate()
    door2.activate()
    door3.activate()

    # Check if a door was clicked and assign it a value
    while not (door1.clicked(pt) or door2.clicked(pt) or door3.clicked(pt)):
        pt = win.getMouse()
        if door1.clicked(pt):
            doorValue = 1
            door2.deactivate()
            door3.deactivate()
        elif door2.clicked(pt):
            doorValue = 2
            door1.deactivate()
            door3.deactivate()
        elif door3.clicked(pt):
            doorValue = 3
            door1.deactivate()
            door2.deactivate()
    
    winCheck(win, winningDoor, doorValue)

def winCheck(win, winningDoor, doorValue):
    # Check for a win
    if doorValue == winningDoor:
        winButton = Button(win, Point(50, 7.5), 80, 10, "You won!")
        winButton.activate()
    else:
        loseButton = Button(win, Point(50, 7.5), 80, 10, """You lose.
The correct door is: {0}.""".format(winningDoor))
        loseButton.activate()
    win.getMouse()

def main():

    Introduction()
    win, door1, door2, door3, shuffleButton, resultButton = createGameWindow()
    playTheGame(win, door1, door2, door3, shuffleButton, resultButton)

main()
