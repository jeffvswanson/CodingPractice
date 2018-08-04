# studentClass.py
# A program that determines which class year a student is in
# based off the number of credits earned.
"""A certain college classifies students according to credits earned. A student
with less than 7 credits is a Freshman. At least 7 credits are required to be a
Sophomore, 16 to be a Junior, and 26 to be classified a Senior. Write a program
that calculates class standing from  the number of credits earned."""

def main():

    print("""This program accepts a student's number of credits as an input and
prints the corresponding class year.
(<7: Freshman, 7-15: Sophomore, 16-25: Junior, >=26: Senior)""")
    try:
        credits = int(input("Please enter the student's earned credits (0+): "))
        if credits >= 26:
            grade = "Senior"
        elif credits >= 16 and credits <= 25:
            grade = "Junior"
        elif credits >= 7 and credits <= 15:
            grade = "Sophomore"
        else:
            grade = "Freshman"
        print("The student with {0} credits is a {1}.".format(credits, grade))
    except (ValueError, SyntaxError):
        print("You need to enter an integer greater than 0. Exiting.")

main()
