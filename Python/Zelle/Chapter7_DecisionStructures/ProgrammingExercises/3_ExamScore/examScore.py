# examScore.py
# A program that accepts a 100-point exam score as an input and uses a decision
# structure to calculate the corresponding grade.
"""A certain CS professor gives 100-point exams that are graded on the scale
90-100:A, 80-89:B, 70-79:C, 60-69:D, <60:F. Write a program that accepts an exam
score as input and uses a decision structure to calculate the corresponding
grade."""

def main():
    print("""This program accepts a 100-point exam score as an input and
calculates the corresponding grade.
(90-100:A, 80-89:B, 70-79:C, 60-69:D, <60:F)""")
    try:
        score = float(input("\nPlease enter the exam score (0-100): "))
        # Assume this can be greater than 100 if professor gives extra credit.
        if score >= 90:
            grade = "A"
        elif score >= 80 and score <=89:
            grade = "B"
        elif score >= 70 and score <=79:
            grade = "C"
        elif score >= 60 and score <=69:
            grade = "D"
        else:
            grade = "F"
        print("The grade for {0} is {1}.".format(score, grade))
    except (ValueError, SyntaxError):
        print("You need to enter a number between 0 and 100. Exiting.")

main()
