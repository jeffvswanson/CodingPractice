# quizScoreHistogram.pyw
# A progam to plot a vertical histogram of student quiz scores from an
# input file.
"""Write a program to draw a quiz score histogram. Your program should read data
from a file. Each line of the file contains a number in the range 0-10. Your
program must count the number of occurrences of each score (0-10) and then draw
a vertical bar chart with a bar for each possible score. For example, if 15
students got an 8, then the height of the bar for 8 should be 15. Hint: Use a
list that stores the count for each possible score."""

from graphics import *

def main():

    # Introduction
    print("""This program counts the number of student test scores
from an input file and plots each student's last name followed by a score
ranging from 0 to 100.""")

    # Create a graphic window to get the file name.
    initialwin = GraphWin("Input File Name", 400, 400)
    initialwin.setBackground("white")
    initialwin.setCoords(0.0, 0.0, 4.0, 4.0)
    # Introduction
    message = Text(Point(2.0, 3.5), \
                   """This program counts the number of student test scores
from an input file and plots each score as a
vertical histogram""").draw(initialwin)
    Text(Point(0.75, 3), "Input file name: ").draw(initialwin)

    infileEntry = Entry(Point(2.25, 3), 20)
    infileEntry.setText("")
    infileEntry.draw(initialwin)

    button = Text(Point(2, 1.5), "Get the file")
    button.draw(initialwin)
    Rectangle(Point(1, 1.0), Point(3, 2)).draw(initialwin)

    initialwin.getMouse()

    infileName = infileEntry.getText()

    initialwin.close()

    # Read the file to create the plot.
    infile = open(infileName, "r")
    numLines = 0
    scores = []

    for line in infile:
        numLines = numLines + 1
        scoreList = list(line.split())
        scores.append(int(scoreList[1]))

    infile.close()

    # Iterate through the scores list to accumulate scores together.
    # Initialize a list with a zero in each score index
    aggregate = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in scores:
        aggregate[i] += 1

    print(aggregate)
    
    # Create a graphics window to plot the quiz scores.
    # Each accumulated score increases the window height by 30 pixels.
    windowHeight = (max(aggregate) + 2) * 30
    win = GraphWin("Student Score Histogram", 400, windowHeight)
    win.setBackground("white")
    winYcoord = windowHeight/10.0
    win.setCoords(0.0, 0.0, 40.0, winYcoord)
    
    # Print the scores arranged along the bottom.
    interval = 38/11
    for i in range(0, 11):
        score = Text(Point((2 + interval * i), 1.5),"{}".format(i))
        score.draw(win)
    # Set the properties of the score bars
    barWidth = interval / 2
    # xll = initial x lower left
    xll = 2
    # yll = initial y lower left
    yll = 3
    
    # counter to index the scores list
    counter = 0
    for i in aggregate:
        # To allow for whitespace at right end
        barHeight = i * 3    
        bar = Rectangle(Point((xll + (counter * interval) - (interval/4)), yll),
                        Point((xll + (counter * interval) + (interval/4)),
                              yll + barHeight))
        bar.setFill("pink")
        bar.draw(win)
        counter += 1

    Text(Point(20.0, winYcoord - 1), "Click to quit.").draw(win)
    win.getMouse()
    win.close()

main()
