# fileWordCount.py
# A program that counts the number of lines, words, and characters in a file.
"""Word Count. A common utility on Unix/Linux systems is a small program called
"wc." This program analyzes a file to determine the number of lines, word, and
characters contained therein. Write your own version of wc. The program should
accept a file name as inpt  and then print three numbers showing the count of
lines, words, and characters in the file."""

def main():

    print("This program counts the number of lines, words, and \
characters in a file.")

    # Get the file name
    infileName = input("Please enter your file name: ")

    # Open the file
    infile = open(infileName, "r")

    # Process each line of the input file
    numLines, numWords, numChars = 0, 0, 0
    for line in infile:
          numLines = numLines + 1
          sentenceList = list(line.split())
          numWords = numWords + len(sentenceList)
          charList = list(line)
          numChars = numChars + len(line)
          
    infile.close()

    print("\nThere are {0} lines in the file.".format(numLines))
    print("\nThere are {0} words in the file.".format(numWords))
    print("\nThere are {0} characters in the file.".format(numChars))
    

main()
