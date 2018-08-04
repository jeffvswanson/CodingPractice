# acronymCreator2.py
# A program that accepts a string and returns the acronym of the string.
"""Do Programming Exercise 4 from Chapter 5 using a function acronym(phrase)
that returns an acronym for a phrase supplied as a string."""

def acronym(phrase):
    acronymList = []
    
    for f in phrase.split():
        acronymList.append(f[0])

    letters = "".join(acronymList)
    return letters

def main():

    print("This program accepts a string and then returns the acronym of the string.")
    phrase = input("Please input the words you want to make an acronym: ")

    letters = acronym(phrase)
        
    print("\nThe acronym is {0}.".format(letters.upper()))

main()
