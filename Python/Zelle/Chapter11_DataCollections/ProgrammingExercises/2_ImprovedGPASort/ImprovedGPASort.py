# improvedGPASort.py
# A program to sort student information by GPA, name, or credits.
"""Extend the gpasort program so that it allows the user to sort a file of
students based on GPA, name, or credits. Your program should prompt for the
input file, the field to sort on, and the output file."""

from gpaClass import Student, makeStudent

def getFileName():
    while True:
        try:
            filename = input("Enter the name of the data file: ")
        except(SyntaxError, NameError, TypeError, ValueError):
            print("You have to enter a valid file path.")
            continue
        else:
            break
    return filename

def howToSort():
    sortChoice = input("How do you want the data sorted? \
    1 = GPA, 2 = name, 3 = credits")
    # Dos a try except test to get the sortChoice
    return sortChoice

def readStudents(filename):
    infile = open(filename, 'r')
    students = []
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students

def writeStudents(students, filename):
    outfile = open(filename, 'w')
    for s in students:
        print("{0}\t{1}\t{2}".
                format(s.getName(), s.getHours(), s.getQPoints()),
            file = outfile)
    outfile.close()

def gpaSort(filename):
    data = readStudents(filename)
    data.sort(key=Student.gpa)

def nameSort(filename):
    data = readStudents(filename)
    data.sort(key=Student.getName)

def creditSort(filename):
    data = readStudents(filename)
    data.sort(key=Student.getHours)

def main():
    print("This program sorts student information by GPA, name, or credits.")
    filename = getFileName()
    sortChoice = howToSort()
    # Do a routine that takes sortChoice and goes to the correct sort returning the information

    filename = input("Enter a name for the output file: ")
    writeStudents(info, filename)
    print("The data has been written to", filename)

if __name__ == '__main__':
    main()