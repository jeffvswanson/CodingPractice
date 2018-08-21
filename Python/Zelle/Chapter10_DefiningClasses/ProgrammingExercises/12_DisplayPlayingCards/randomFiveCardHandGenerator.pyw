# randomFiveCardHandGenerator.pyw
# A program to display a hand of five random cards.
"""Extend your card class from Chapter 10 Programming Exercise 11 with a 
draw(self, win, center) method that displays a hand of five random cards. Hint:
The easiest way to dio this is to search the Internet for a free set of card
images and use the Image object in the graphics library to display them."""

from random import randrange
from graphics import GraphWin, Point, Image, Text

from button import Button
from playingCardClass import playingCard

def Introduction():
    # Print a description of what the program does
    win = GraphWin("Introduction", 300, 300)
    win.setBackground("green2")
    readButton = Button(win, Point(150, 250), 150, 25, "I read the intro.")
    readButton.activate()
    ruleBox = Button(win, Point(150, 125), 225, 100, """This program prints five
random playing cards""")
    ruleBox.activate()
    # Don't move on until the intro has been acknowledged
    pt = win.getMouse()
    while not readButton.clicked(pt):
        if readButton.clicked(pt):
            break
        else:
            pt = win.getMouse()

def displayCards():
    # List of suits in a playing card hand. c = clubs, d = diamonds, etc.
    suitList = ["c", "d", "h", "s"]

    # Create the application window
    win = GraphWin("Five Card Hand Generator", 375, 340)
    win.setBackground("green2")

    # Horizontal and vertical center of the card in pixels
    xCenter = 112
    yCenter = 160
    # Generate and draw the cards in the window
    for card in range(0, 5):
        rank = randrange(1,13)
        j = randrange(0, 3)
        suit = suitList[j]
        card = playingCard(rank, suit)
        # Prepare the filename
        filename = card.__str__().title()
        filename = filename.replace(" ","")
        filename = "C:\\Users\\Tarkakagogue\\Documents\\CodingPractice\\Python\
\Zelle\\Chapter10_DefiningClasses\\ProgrammingExercises\
\\12_DisplayPlayingCards\\PlayingCardImages\\{0}.png".format(filename)
        # print(filename)
        xCenter = 25 + xCenter
        anchorPoint = Point(xCenter, yCenter)
        cardImage = Image(anchorPoint, filename)
        cardImage.draw(win)
        message = Text(Point(375/2, 330), "Click for next card").draw(win)
        win.getMouse()
        message.undraw()
    Text(Point(375/2, 330), "Click to Quit").draw(win)
    win.getMouse()
        

def main():
    
    Introduction()
    displayCards()

main()
