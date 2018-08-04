# examScoring.py
# A program that accepts a quiz score as an input and prints out the
# corresponding grade.
# 90-100:A, 80-89:B, 70-79:C, 60-69:D, <60:F

def main():

    print("Quiz scoring is a program that accepts a quiz score as an input and \
prints out the corresponding grade.")
    print("90-100:A, 80-89:B, 70-79:C, 60-69:D, <60:F")
    score = eval(input("Please enter the quiz score: "))
    grades = ["F", "F", "F", "F", "F", "F", "F", "F", "F", "F",\
              "F", "F", "F", "F", "F", "F", "F", "F", "F", "F",\
              "F", "F", "F", "F", "F", "F", "F", "F", "F", "F",\
              "F", "F", "F", "F", "F", "F", "F", "F", "F", "F",\
              "F", "F", "F", "F", "F", "F", "F", "F", "F", "F",\
              "F", "F", "F", "F", "F", "F", "F", "F", "F", "F",\
              "D", "D", "D", "D", "D", "D", "D", "D", "D", "D",\
              "C", "C", "C", "C", "C", "C", "C", "C", "C", "C",\
              "B", "B", "B", "B", "B", "B", "B", "B", "B", "B",\
              "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A"]

    grade = grades[score]

    print("\nThe quiz grade is {0}".format(grade))

main()
