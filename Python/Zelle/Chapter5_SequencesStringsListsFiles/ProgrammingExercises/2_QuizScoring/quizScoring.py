# quizScoring.py
# A program that accepts a quiz score as an input and prints out
# the corresponding grade.
# 5-A, 4-B, 3-C, 2-D, 1-F, 0-F
"""A certain CS professor gives 5-point quizzes that are graded on the scale
5-A, 4-B, 3-C, 2-D, 1-F, 0-F. Write a progra that accepts a quiz score as an
input and prints out the corresponding grade."""

def main():

    print("Quiz scoring is a program that accepts a quiz score as an input \
and prints out the corresponding grade.")
    print("5-A, 4-B, 3-C, 2-D, 1-F, 0-F")
    score = int(input("Please enter the quiz score: "))
    grades = ["F", "F", "D", "C", "B", "A"]

    grade = grades[score]

    print("\nThe quiz grade is {0}".format(grade))

main()
