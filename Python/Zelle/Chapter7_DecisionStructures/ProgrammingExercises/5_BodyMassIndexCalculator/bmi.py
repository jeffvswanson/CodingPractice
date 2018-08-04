# bmi.py
# A program that accepts a person's weight in pounds and height in inches to
# determine their BMI and notify if they are in the low, healthy, or high
# category.
"""The body mass index (BMI) is calculated as a person's weight (in pounds)
times 720, divided by the square of the person's height (in inches). A BMI in
the range 19-25, inclusive, is considered healthy. Write a program that
calculates a person's BMI and prints a message telling whether they are above,
within, or below the healthy range."""

def calcBMI(height, weight):

    BMI = weight * 720 / height ** 2

    if BMI < 19:
        BMImessage = "too low"
    elif BMI >= 19 and BMI <= 25:
        BMImessage = "healthy"
    else:
        BMImessage = "too high"        

    return BMI, BMImessage

def main():
    print("This program determines if a person is in a healthy BMI range.")
    try:
        height = float(input("Please enter the person's height in inches: "))
        weight = float(input("Pleaes enter the person's weight in pounds: "))

        BMI, BMImessage = calcBMI(height, weight)

        print("Your BMI is {0:0.1f} and {1}.".format(BMI, BMImessage))
    except (ValueError, SyntaxError):
        print("You need to enter a number. Exiting.")

main()
