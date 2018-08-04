# event_loop2.py --- color changing window

from graphics import *

def handleKey(k, win):
    if k == "r":
        win.setBackground("pink")
    elif k == "w":
        win.setBackground("white")
    elif k == "g":
        win.setBackground("lightgray")
    elif k == "b":
        win.setBackground("lightblue")

def handleClick(pt, win):
    pass

def main():
    win = GraphWin("Color Window", 500, 500)

    # Event Loop: handle key presses until user presses the 'q' key.
    while True:
        key = win.checkKey()
        if key == "q": # loop exit
            break

        # Process the key
        if key:
            handleKey(key, win)

        pt = win.checkMouse()
        if pt:
            handleClick(pt, win)

    # exit program
    win.close()

main()