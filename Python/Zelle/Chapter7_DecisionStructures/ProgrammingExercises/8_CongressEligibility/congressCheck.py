# congressCheck.py
# A program that accepts a person's age and years of citizenship to determine 
# eligibility for the House and Senate.
"""A person is eligible to be a US senator if they are at least 30 years old
and have been a US citizen for at least 9 years. To be a US representative
these numbers are 25 and 7, respectively. Write a program that accepts a
person's age and years of citizenship as input and outputs their eligibility
for the Senate and House."""


def check(age, citizen):

    if age >= 30 and citizen >= 9:
        message = "This person is eligible to serve in both the House and \
Senate."
    elif age >= 25 and citizen >= 7:
        message = "This person is eligible to only serve in the House of \
Representatives."
    else:
        message = "This person is ineligible to serve in Congress."
	
    return message

def main():

    print("This program checks a person's age and years of citizenship to see \
if they are eligible to serve in the U.S. House of Representatives or \
Senate.")
    try:
        age = int(input("\nPlease enter the person's age: "))
        citizen = int(input("Please enter the person's years of U.S. \
citizenship: "))

        message = check(age, citizen)

        print(message)
    except (ValueError, SyntaxError):
        print("You need to enter whole numbers. Exiting.")

main()
