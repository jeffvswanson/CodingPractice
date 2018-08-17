# threebuttonmonte2.py
# An improvement to threebuttonmonte.py by allowing the user
# to click a button to quit and record results from mulpiple rounds.
"""Extend the program from Chapter 10 Programming Exercise 3 by allowing the 
user to play multiple rounds and displaying the number of wins and losses. Add
a "Quit" button for ending the game."""

from random import randrange
from graphics import *

from button import Button

def Introduction():
    # Introduction and explain the rules
    win = GraphWin("Three Button Monte", 400, 400)
    win.setCoords(0, 0, 40, 40)
    win.setBackground("green2")
    quitButton = Button(win, Point(20, 4), 8, 4, "Quit")
    quitButton.activate()
    readButton = Button(win, Point(20, 10), 24, 4, "I read the rules")
    readButton.activate()
    rulesBox = Button(win, Point(20, 25), 32, 22, """One door is the winner. 
You have to pick it.""")
    rulesBox.activate()
    # Don't move on until the rules are acknowledged.
    pt = win.getMouse()
    while not readButton.clicked(pt):
        if readButton.clicked(pt):
            break
        elif quitButton.clicked(pt):
            closeProgram(win)
        else:
            pt = win.getMouse()
    win.close()

def playTheGame():
    # Draws the window the doors will be on.
    win = GraphWin("Three Button Monte", 260, 380)
    win.setCoords(0, 0, 26, 38)
    win.setBackground("green2")
    # Draw the win/loss ribbon
    winLoss = Button(win, Point(13, 35), 22, 2, "Wins: 0\tLosses: 0")
    winLoss.deactivate()
    # Draw the doors
    door1 = Button(win, Point(5, 25), 6, 14, "Door 1")
    door2 = Button(win, Point(13, 25), 6, 14, "Door 2")
    door3 = Button(win, Point(21, 25), 6, 14, "Door 3")
    # Draw a button to shuffle the doors
    shuffleButton = Button(win, Point(13, 15), 14, 2, "Shuffle Doors")
    shuffleButton.activate()

    resultButton = Button(win, Point(13, 10), 22, 4, "Result")
    resultButton.deactivate()
    # Draw the quit button
    quitButton = Button(win, Point(13, 4), 10, 4, "Quit")
    quitButton.activate()

    # Initalize wins and losses for the results banner
    wins = 0
    losses = 0

    pt = win.getMouse()
    while not quitButton.clicked(pt):

        # Have the user shuffle the winning door
        winningDoor = randrange(1,4)
        if shuffleButton.clicked(pt):
            shuffle(win, shuffleButton, door1, door2, door3)
        else:
            while not shuffleButton.clicked(pt):
                pt = win.getMouse()
                if shuffleButton.clicked(pt):
                    # Deactivate the shuffleButton and activate the doors
                    shuffle(win, shuffleButton, door1, door2, door3)
                else:
                    pt = win.getMouse()

        # Check if a door was clicked and assign it a value
        while not (door1.clicked(pt) or door2.clicked(pt) or door3.clicked(pt) or quitButton.clicked(pt)):
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
            elif quitButton.clicked(pt):
                closeProgram(win)
        
        # Check for a win
        if doorValue == winningDoor:
            result = "You won!"
            wins = wins + 1
            resultsBanner(win, wins, losses, resultButton, winLoss, result)
        else:
            result = "You lose. \nThe correct door is: {0}.".format(winningDoor)
            losses = losses + 1
            resultsBanner(win, wins, losses, resultButton, winLoss, result)

        # Reset the game board
        door1.deactivate()
        door2.deactivate()
        door3.deactivate()
        shuffleButton.activate()
        pt = win.getMouse()
        resultButton = Button(win, Point(13, 10), 22, 4, "Result")
        resultButton.deactivate()
            
    closeProgram(win)   


def shuffle(win, shuffleButton, door1, door2, door3):
    # Deactivate the shuffleButton and activate the doors
    shuffleButton.deactivate()
    door1.activate()
    door2.activate()
    door3.activate()

def resultsBanner(win, wins, losses, resultButton, winLoss, result):

    resultButton = Button(win, Point(13, 10), 22, 4, result)
    resultButton.activate()

    winLoss = Button(win, Point(13, 35), 22, 2, "Wins: {0}\tLosses: {1}".format(wins, losses))
    winLoss.activate()

def closeProgram(win):
    win.close()
    sys.exit()

def main():

    Introduction()
    playTheGame()

main()
