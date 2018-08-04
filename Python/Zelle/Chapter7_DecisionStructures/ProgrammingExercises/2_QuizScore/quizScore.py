# quizScore.py
# A program that accepts a quiz score as an input and uses a decision structure
# to calculate the corresponding grade.
"""A certain CS professor gives five-point quizzes that are graded on the scale
5-A, 4-B, 3-C, 2-D, 1-F, 0-F. Write a program that accepts a quiz score as an
input and uses a decision structure to calculate the corresponding grade."""

def main():

    print("""This program accepts a quiz score as an input and calculates
the corresponding grade. (5-A, 4-B, 3-C, 2-D, 1-F, 0-F)""")
    try:
        score = int(input("\nPlease enter the quiz score (0-5): "))
        # Assume this can be greater than 6 if CS professor gives extra credit
        if score >= 5:
            grade = "A"
        elif score == 4:
            grade = "B"
        elif score == 3:
            grade = "C"
        elif score == 2:
            grade = "D"
        else:
            grade = "F"
        print("The grade for {0} is {1}.".format(score, grade))
    except (ValueError, SyntaxError):
        print("You need to enter an integer of 0 through 5. Exiting.")

main()
