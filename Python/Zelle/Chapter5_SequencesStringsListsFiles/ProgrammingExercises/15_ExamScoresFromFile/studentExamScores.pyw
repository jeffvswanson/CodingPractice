# studentExamScores.pyw
# A progam to plot a horizontal bar chart of student exam scores from an
# input file. The program counts the number of students in the file and 
# plots each student's last name followed by a score ranging from
# 0 to 100.
"""Write a program to plot a hozontal bar chart of student exam scores. Your
program should get input from a file. The first line of the file contains the
count of the number of students in the file, and each subsequent line contains
a student's last name followed by a score in the range 0-100. Your program
should draw a horizontal rectangle for each student where the length of the bar
represents the student's score. The bars should all line up on their  left-hand
edges. Hint; Use the number of students to determine the size of the window and
its coordinates. Bonus: label the bars at the left end with the students'
names."""

from graphics import *

def main():

    # Create a graphic window to get the file name.
    initialwin = GraphWin("Input File Name", 400, 400)
    initialwin.setBackground("white")
    initialwin.setCoords(0.0, 0.0, 4.0, 4.0)
    # Introduction
    message = Text(Point(2.0, 3.5), \
                   """This program counts the number of student test scores
from an input file and plots each student's last
name followed by a score ranging from 0 to 100.""").draw(initialwin)
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
    names = []
    scores = []

    for line in infile:
        numLines = numLines + 1
        scoreList = list(line.split())
        names.append(scoreList[0])
        scores.append(float(scoreList[1]))

    infile.close()

    # Create a graphics window to plot the students exam scores.
    # Each name increases the window height by 30 pixels.
    windowHeight = numLines * 30
    win = GraphWin("Student Score Chart", 400, windowHeight)
    win.setBackground("white")
    winYcoord = windowHeight/10.0
    win.setCoords(0.0, 0.0, 40.0, winYcoord)
    
    # Print the names on the graph aligned to the left.
    # Truncate names over 12 characters.
    interval = 2
    i = winYcoord - interval
    # Set the properties of the score bars
    barHeight = winYcoord/numLines
    
    # counter to index the scores list
    counter = 0
    for name in names:
        print(name)
        Text(Point(5, i), name[0:11].ljust(12)).draw(win)
        # Draw horizontal bars for score aligned to the left
        xll = 12
        # To allow for whitespace at right end
        barLength = (scores[counter]*(40 - 13)) / 100    
        bar = Rectangle(Point(xll, (i - interval/4)), Point((xll + barLength), \
                                                   (i + interval/4)))
        bar.setFill("orange")
        bar.draw(win)
        i -= interval
        counter += 1

    Text(Point(20.0, 1.5), "Click to quit.").draw(win)
    win.getMouse()
    win.close()

main()
