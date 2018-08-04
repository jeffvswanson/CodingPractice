# oldMacdonald.py
# A program which prints the lyrics of Old MacDonald.
"""Write a program to print the lyrics of the song "Old MacDonald." Your program
should print the lyrics for five different animals, similar to the example verse
below:

    Old MacDonald had a farm, Ee-igh, Ee-igh Oh!
    And on that farm he had a cow, Ee-igh, Ee-igh, Oh!
    With a moo, moo here and a moo, moo there.
    Here a moo, there a moo, everywhere a moo, moo.
    Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!"""

def stanza(animal, sound):
    for i in range(len(animal)):
        animal[i] = animal[i]
        sound[i] = sound[i]
        print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
        print("And on that farm he had a {0}, Ee-igh, Ee-igh, Oh!"\
              .format(animal[i]))
        print("With a {0}, {0} here and a {0}, {0} there.".format(sound[i]))
        print("Here a {0}, there a {0}, everywhere a {0}, {0}.".format(sound[i]))
        print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!\n")
        

def song():
    animals = ["cow", "pig", "horse", "chicken", "goose"]
    sounds = ["moo", "oink", "neigh", "cluck", "honk"]
    stanza(animals, sounds)

song()

    
    
    
