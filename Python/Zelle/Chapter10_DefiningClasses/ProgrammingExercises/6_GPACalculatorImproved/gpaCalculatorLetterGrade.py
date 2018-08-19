# gpaCalculatorLetterGrade.py
# A program to calculate a student's GPA using letter grades as input.
"""Extend Chapter 10 Programming Exercise 5 by implementing an addLetterGrade 
method. This is similar to addGrade except that it accepts a letter grade as
a string (instead of gradePoint). Use the updated class to improve the GPA
calculator by allowing the entry of letter grades."""

from studentRecord import Student

def Intro():
    print("This program allows you to record a student's grade for a course \
and the credits the course was worth to get the student's GPA.")
    studentName = input("Enter name of the student: ")

    return studentName

def inputGrades(studentName):
    pupil = Student(studentName, 0, 0, 0, 0, "")
    grade = "F"
    creditHours = 0
    while grade != "q":
        pupil.addLetterGrade(grade, creditHours)  
        try:
            grade = input("Please enter the letter grade (q to quit): ")
            if grade == "q":
                break
            elif any(char.isdigit() for char in grade):
                print("You have to enter a letter grade.")
                continue
        except(SyntaxError, NameError, TypeError, ValueError):
            print("You have to enter a letter grade.")
            continue
        while True:
            try:
                creditHours = float(input(
                "Please enter the credits the course is worth: "))
            except(SyntaxError, NameError, TypeError, ValueError):
                print("You have to enter a positive number greater than zero.")
                continue
            if creditHours <= 0:
                print("You have to enter a positive number greater than zero.")
                continue
            else: 
                break
    return pupil
  
def main():

    # Create a new student object with 0 credits and 0 quality points
    studentName = input("Enter name of the student: ")
    # Prompt the user to input course information (gradepoint and credits)
    pupil = inputGrades(studentName)
    # Print the final GPA achieved.
    print("{0}'s GPA is {1}.".format(pupil.getName(), pupil.gpa()))
        
main()
