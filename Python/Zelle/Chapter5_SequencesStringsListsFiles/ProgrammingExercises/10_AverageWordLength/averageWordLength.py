# averageWordLength.py
# A program that counts the average length of words in a sentence.
"""Write a program that calculates the average word length in a sentence entered
by the user."""

def main():

    print("This program counts the number of words in a sentence.")
    sentence = input("Please enter your sentence: ")
    sentenceList = list(sentence.split())
    numWords = len(sentenceList)

    wordLength = 0

    for f in sentenceList:
        wordLength = wordLength + len(f)

    avgLength = wordLength/numWords

    print("\nThere average length of words in the sentence is {0}."\
          .format(avgLength))
    

main()
