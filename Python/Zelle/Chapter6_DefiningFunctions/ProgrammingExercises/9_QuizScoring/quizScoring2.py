# quizScoring2.py
# A program that accepts a quiz score as an input and prints out
# the corresponding grade.
# 5-A, 4-B, 3-C, 2-D, 1-F, 0-F
"""Do Programming Exercise 3 from Chapter 5 using a function grade(score) that
returns the letter grade for a score."""

def grade(score):
    grades = ["F", "F", "D", "C", "B", "A"]
    grade = grades[score]
    return grade

def main():

    print("Quiz scoring is a program that accepts a quiz score as an input and prints out the corresponding grade.")
    print("5-A, 4-B, 3-C, 2-D, 1-F, 0-F")
    score = int(input("Please enter the quiz score: "))
    
    g = grade(score)
    
    print("\nThe quiz grade is {0}.".format(g))

main()
