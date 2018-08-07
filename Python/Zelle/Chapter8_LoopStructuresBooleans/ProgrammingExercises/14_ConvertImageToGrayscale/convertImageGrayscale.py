# convertImageGrayscale.py
# A program that converts a user supplied image to grayscale.
"""Write a program that converts a color image to grayscale. The user supplies
the name of a file containing a GIF or PPM image, and the program loads the 
image and displays the file. At the click of a mouse, the program converts the
image to grayscale. The user is then prompted for a file name to store the 
grayscale image in.
    You will probably want to go back and review the Image object from the
graphics library (Section 4.8.4). The basic idea of converting the image is to 
go through it pixel by pixel and convert each one from color to an appropriate
shade of gray. A gray pixel is created by setting its red, green, and blue
components to have the same brightness. So color_rgb(0, 0, 0) is black, 
color_rgb(255, 255, 255) is white, and color_rgb(127, 127, 127) is gray
"halfway" between. You should use a weighted average of the original RGB values
to determine the brightness of the gray. Here is the pseudocode for the 
grayscale algorithm:
    for each row in the image:
        for each column in the image:
            r, g, b = get pixel information for the current row and column
            brightness = int(round(0.299r + 0.587g + 0.114b))
            set pixel color to color_rgb(brightness, brightness, brightness)
        update the image # to see progress row by row

    Note: The pixel operations in the Image class are rather slow, so you will 
want to use relatively small images (not 12 megapixels) to test your 
program."""

from graphics import *

def getPicture():
    # Create a graphic window to get the file name.
    win = GraphWin("Input File Name", 400, 400)
    win.setBackground("white")
    win.setCoords(0.0, 0.0, 4.0, 4.0)
    # Introduction
    message = Text(Point(2.0, 3.5), \
"""This program gets a color image 
and converts it to grayscale.""").draw(win)
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

    win = GraphWin("Grayscale Converter", w, h)
    photo.draw(win)

    message = Text(Point(w/2, h/3), """Click to start
    grayscale conversion.""")
    message.setSize(36)
    message.setTextColor("Orange")
    message.draw(win)

    win.getMouse()
    message.undraw()
    grayscaleConverter(photo, win)

    return photo, win

def grayscaleConverter(photo, win):
    w = photo.getWidth()
    h = photo.getHeight()
    for row in range(0, h):
        for col in range(0, w):
            r, g, b = photo.getPixel(col, row)
            brightness = int(round(0.299*r + 0.587*g + 0.114*b))
            photo.setPixel(col, row, \
                color_rgb(brightness, brightness, brightness))
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
    # Display the file and convert the image to grayscale
    photo, win = showPhoto(infileName)
    # Open a new window to let the user save the photo
    savePhoto(photo)
    # Let the user admire the newly saved photo
main()