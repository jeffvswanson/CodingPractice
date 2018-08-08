# convertImageNegative.py
# A program that converts a user supplied image to its negative.
"""Write a program to convert an image to its color negative. The general form 
of the program will be similar to that of Chapter 8, Programming Exercise 14. 
The negative of a pixel is formed by subtracting each color value from 255. So
the new pixel color is color_rgb(255-r, 255-g, 255-b)."""

from graphics import *

def getPicture():
    # Create a graphic window to get the file name.
    win = GraphWin("Input File Name", 400, 400)
    win.setBackground("white")
    win.setCoords(0.0, 0.0, 4.0, 4.0)
    # Introduction
    message = Text(Point(2.0, 3.5), \
"""This program gets a color image 
and converts it to negative.""").draw(win)
    Text(Point(0.75, 3), "Input file name: ").draw(win)
    infileEntry = Entry(Point(2.25, 3), 20)
    infileEntry.draw(win)

    button = Text(Point(2, 1.5), "Get the file")
    button.draw(win)
    Rectangle(Point(1, 1.0), Point(3, 2)).draw(win)

    # Initialize p to immediately execute the while loop
    p = Point(0, 0)
    infileEntry.setText("")
    while not((p.getX() >= 1 and p.getX() <= 3) and \
    (p.getY() >= 1.0 and p.getY() <= 2)):

        p = win.getMouse()
        # Do nothing if the click is not in the "Get file" button
        if not((p.getX() >= 1 and p.getX() <= 3) and \
    (p.getY() >= 1.0 and p.getY() <= 2)):
            pass
        else:
            try:
                infileName = infileEntry.getText()
                # Files have a period before the file type
                if infileName == "" or not("." in infileName):
                    # Reset p to keep the window open.
                    p = Point(0, 0)
                    message.setText("You have to enter a valid file name.")
                    infileEntry.setText("")
                    continue
            except (SyntaxError, NameError, TypeError, ValueError):
                message.setText("You have to enter a valid file name.")
                infileEntry.setText("")
                # You don't want the window closing inadvertently, so reset p.
                p = Point(0, 0)
                continue

    win.close()

    return infileName

def showPhoto(infileName):
    photo = Image(Point(0,0), infileName)
    w = photo.getWidth()
    h = photo.getHeight()
    photo.move(w/2, h/2)

    win = GraphWin("Negative Converter", w, h)
    photo.draw(win)

    message = Text(Point(w/2, h/3), """Click to start
    negative conversion.""")
    message.setSize(36)
    message.setTextColor("Orange")
    message.draw(win)

    win.getMouse()
    message.undraw()
    negativeConverter(photo, win)

    return photo, win

def negativeConverter(photo, win):
    w = photo.getWidth()
    h = photo.getHeight()
    for row in range(0, h):
        for col in range(0, w):
            r, g, b = photo.getPixel(col, row)
            photo.setPixel(col, row, \
                color_rgb(255 - r, 255 - g, 255 -b))
        # Update each row to show progress
        win.update()

def savePhoto(photo):
    # Create a graphic window to allow the user to save the photo.
    win = GraphWin("Save Photo", 400, 400)
    win.setBackground("white")
    win.setCoords(0.0, 0.0, 4.0, 4.0)
    # Introduction
    message = Text(Point(2.0, 3.5), \
"""Do you want to save your photo? """).draw(win)
    Text(Point(0.75, 3), "Save file as: ").draw(win)
    saveFileEntry = Entry(Point(2.25, 3), 20)
    saveFileEntry.draw(win)

    button = Text(Point(2, 1.5), "Save the file")
    button.draw(win)
    Rectangle(Point(1, 1.0), Point(3, 2)).draw(win)

    # Initialize p to immediately execute the while loop
    p = Point(0, 0)
    saveFileEntry.setText("")
    while not((p.getX() >= 1 and p.getX() <= 3) and \
    (p.getY() >= 1.0 and p.getY() <= 2)):

        p = win.getMouse()
        # Do nothing if the click is not in the "Save file" button
        if not((p.getX() >= 1 and p.getX() <= 3) and \
    (p.getY() >= 1.0 and p.getY() <= 2)):
            pass
        else:
            try:
                saveFileName = saveFileEntry.getText()
                # Files have a period before the file type
                if saveFileName == "" or not("." in saveFileName):
                    # Reset p to keep the window open.
                    p = Point(0, 0)
                    message.setText("You have to enter a valid file name.")
                    saveFileEntry.setText("")
                    continue
            except (SyntaxError, NameError, TypeError, ValueError):
                message.setText("You have to enter a valid file name.")
                saveFileEntry.setText("")
                # You don't want the window closing inadvertently, so reset p.
                p = Point(0, 0)
                continue
    photo.save(saveFileName)
    win.close()

def main():
    # Get the input file from the user
    infileName = getPicture()
    # Display the file and convert the image to negative
    photo, win = showPhoto(infileName)
    # Open a new window to let the user save the photo
    savePhoto(photo)
    # Let the user admire the newly saved photo
main()