# theAntsGoMarching.py
# A program which prints the lyrics of The Ants Go Marching.
"""Write a program to print the  yrics for ten verses of "The Ants Go Marching."
A couple of sample verses are given below. You may choose your own activity for
the "little one" in each vers, but be sure to choose something that makes the
rhyme work (or almost work)."""

def stanza(number, activity):
    for i in range(len(number)):
        number[i] = number[i]
        activity[i] = activity[i]
        print("The ants go marching {0} by {0}, hurrah!, hurrah!"\
              .format(number[i]))
        print("The ants go marching {0} by {0}, hurrah!, hurrah!"\
              .format(number[i]))
        print("The ants go marching {0} by {0},".format(number[i]))
        print("The little one stops to {0},".format(activity[i]))
        print("And they all go marching down...")
        print("In the ground...")
        print("To get out...")
        print("Of the rain.")
        print("Boom! Boom! Boom!\n")
        

def song():
    number = ["one", "two", "three", "four", "five", "six", "seven",\
              "eight", "nine", "ten"]
    activity = ["suck his thumb", "tie his shoe", "take a knee",\
                "shut the door", "jump and jive", "pick up sticks",\
                "count to eleven", "shut the gate", "draw a line",\
                "shout 'Let's do it again!"]
    stanza(number, activity)

song()

    
    
    
