# gpaCalculator.py
# A program to calculate a student's GPA.
"""Modify the Student class from the chapter by adding a mutator method that 
records a grade for the student. Here is the specification of the new method:
    addGrade(self, gradePoint, credits) gradePoint is a float that represents
a grade (e.g., A = 4.0, A- = 3.7, B+ = 3.3, etc.), and credits is a float 
indicating the number of credit hours for the class. Modify the student object
by adding this grade information.
    Use the updated class to implement a simple program for calculating GPA. 
Your program should create a new student object that has 0 credits and 0 
quaility points (the name is irrelevant). Your program should then prompt the 
user to enter course information (gradePoint and credits) for a series of 
courses, and then print out the final GPA achieved."""

from studentRecord import Student

def Intro():
    print("This program allows you to record a student's grade for a course \
and the credits the course was worth to get the student's GPA.")
    studentName = input("Enter name of the student: ")

    return studentName

def inputGrades(studentName):
    pupil = Student(studentName, 0, 0, 0, 0, 0)
    grade = 0
    creditHours = 0
    while grade != -1:
        pupil.addGrade(grade, creditHours) 
        try:
            grade = float(input("Please enter the grade as a decimal between 0 \
and 4.0 (-1 to quit): "))
            if grade == -1:
                break
        except(SyntaxError, NameError, TypeError, ValueError):
            print("You have to enter a number between 0 and 4.")
            continue
        creditHours = float(input(
            "Please enter the credits the course is worth: "))
    return pupil
  
def main():

    # Create a new student object with 0 credits and 0 quality points
    studentName = Intro()
    # Prompt the user to input course information (gradepoint and credits)
    pupil = inputGrades(studentName)
    # Print the final GPA achieved.
    print("{0}'s GPA is {1}.".format(pupil.getName(), pupil.gpa()))
        
main()
