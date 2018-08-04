# acronymCreator.py
# A program that accepts a string and returns the acronym of the string.
"""An acronym is a word formed by taking the first letters of the words in a
phrase and making a word from them. For example, RAM is an acronym for "random
access memory." Write a program that allows the user to type in a phrase and
then outputs the acronym for that phrase. Note: The acronym should be all
uppercase, even if the words in the phrase are not capitalized."""

def main():

    print("This program accepts a string and then returns the acronym of the \
string.")
    phrase = input("Please input the words you want to make an acronym: ")

    acronym = ""
    phraseSplit = phrase.split()
    for f in phraseSplit:
        acronym = acronym + f[0]

    print("\nThe acronym is {0}.".format(acronym.upper()))

main()
