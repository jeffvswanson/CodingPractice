# sentenceLengthCounter.py
# A program that counts the number of words in a sentence.
"""Write a program that calculates the average word length in a sentence entered
by the user."""

def main():

    print("This program counts the number of words in a sentence.")
    sentence = input("Please enter your sentence: ")
    sentenceList = list(sentence.split())
    numWords = len(sentenceList)

    print("\nThere are {0} words in the sentence.".format(numWords))

main()
