# studentRecord.py
""" A class that creates a student with name, credit hours, quality points, GPA,
and allows the user to add a grade to the student's record."""

class Student:

    def __init__(self, name, hours, qpoints, gradePoint, credits, letterGrade):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)
        self.gradePoint = float(gradePoint)
        self.credits = float(credits)
        self.letterGrade = str(letterGrade)

    def getName(self):
        """Provide the student's name."""
        return self.name

    def getHours(self):
        """Provide the number of hours a student has completed."""
        return self.hours

    def getQPoints(self):
        "Provide the number of quality points a student has earned."""
        return self.qpoints

    def gpa(self):
        """Calculate a student's grade point average."""
        if self.credits == 0:
            return
        else:
            return self.qpoints/self.credits

    def addGrade(self, gradePoint, credits):
        """Add a grade to the student's record. Requires the numeric
    grade point received and the number of credits the course was worth
    as parameters."""
        self.qpoints = self.qpoints + (gradePoint * credits)
        self.credits = self.credits + credits
        return self.qpoints, self.credits

    def addLetterGrade(self, letterGrade, credits):
        """Add a letter grade to the student's record. Requires the letter grade
    received and the number of credits the course was worth as parameters."""
        if letterGrade == "A":
            letterGrade = 4.0
        elif letterGrade == "B":
            letterGrade = 3.0
        elif letterGrade == "C":
            letterGrade = 2.0
        elif letterGrade == "D":
            letterGrade = 1.0
        else:
            letterGrade = 0.0
        self.qpoints = self.qpoints + (letterGrade * credits)        
        self.credits = self.credits + credits
        return self.qpoints, self.credits
