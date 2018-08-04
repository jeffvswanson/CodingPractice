# fineCalculator.py
# A program that accepts a speed limit and a clocked speed and either prints a
# message indicating the speed was legal or prints the amount of the fine, if
# the speed is illegal.
"""The speeding ticket fine policy in Podunksville is $50 plus $5 for each mph
over the limit plus a penalty of $200 for any speed over 90 mph. Write a
program that accepts a speed limit and a clocked speed and either prints a
message indicating the speed was legal or prints the amount of the fine, if the
speed is illegal."""

def calcFine(limit, speed):

    penalty = 50
    mphPenalty = 5
    penaltyAt90 = 200

    if speed >= 90:
        fine = penalty + (speed - limit) * mphPenalty + penaltyAt90
        message = "The fine is ${0:0.2f}.".format(fine)
    elif speed < 90 and speed > limit:
        fine = penalty + (speed - limit) * mphPenalty
        message = "The fine is ${0:0.2f}.".format(fine)
    else:
        message = "The clocked speed was legal."

    return message

def main():

    print("""This program accepts a speed limit and a clocked speed.
Then prints if the speed was legal or the amount of the fine if the speed was
illegal.""")
    try:
        limit = float(input("\nPlease enter the speed limit: "))
        speed = float(input("Please enter the suspect's speed: "))
        
        message = calcFine(limit, speed)

        print(message)
    except (ValueError, SyntaxError):
        print("You need to enter a number greater than zero! Exiting.")

main()
