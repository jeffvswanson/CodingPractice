# timeToDoubleInvestment.py
# A program that calculates how long it takes for an investment to double at a 
# given interest rate.
"""Write a program that uses a while loop to determine how long it takes for an
investment to double at a given interest rate. The input will be an annualized
interest rate, and the output is the number of years it takes an investment to
double. Note: The amount of the initial investment does not matter; you can
use $1."""

def getAPR():
	try:
		apr = float(input("Please enter the interest rate as a decimal: "))
	except (SyntaxError, NameError, TypeError, ValueError) as err:
		print("You have to enter a decimal number for the APR. Exiting.")
		print(err.args)
		quit(0)
	if apr <= 0:
		print("Investments can't double if they're not greater than zero. \
Exiting.")
		quit(0)
	return apr

def result(apr, years):
	if years < 1:
		print("The amount of time it will take to double the initial \
investment at {0:.1%} APR is {1} of a year.".format(apr, years))
	elif years == 1:
		print("The amount of time it will take to double the initial \
investment as {0:.1%} APR is 1 year.".format(apr))
	else:
		print("The amount of time it will take to double at a {0:.1%} APR is {1} \
years.".format(apr, years))

def main():

	print("This program calculates how long it takes for an investment to \
double at a given interest rate in years.")

	apr = getAPR()
	# Initialize the number of years to zero. Initialize the principal.
	initPrincipal = 1
	principal = initPrincipal
	years = 0
	while principal <= (initPrincipal * 2):
		principal = principal + (principal * apr)
		years = years + 1
	
	# Print a grammatically correct sentence for year number.
	result(apr, years)
main()
