# event_loop4.py --- color changing window
"""Modify the event_loop3 program to use the <Esc> key as described in the
text. When the user types into an Entry box, hitting <Esc> should cause the
Entry to disappear and discard whatever text may have been typed in the box."""

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
    # Create an entry for user to type in
    entry = Entry(pt, 10)


    # Go modal: loop until user types <Enter> key
    while True:
        entry.draw(win)
        key = win.getKey()
        if key == "Escape":
            entry.undraw()
            break
        if key == "Return": break
        
    # Undraw the entry and create and draw Text()
    entry.undraw()
    typed = entry.getText()
    Text(pt, typed).draw(win)

    # Clear (ignore) any mouse click that occurred during text entry
    win.checkMouse()

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