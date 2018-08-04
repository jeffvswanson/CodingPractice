# average3.py
# An example of a sentinel loop

def main():
	total = 0.0
	count = 0
	x = float(input("Enter a number to average (negative to quit): "))
	while x >= 0:
		total = total + x
		count = count + 1
		x = eval(input("Enter a number to average (negative to quit): "))
	print("\nThe average of the numbers is", total / count)

main()