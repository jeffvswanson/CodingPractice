# average2.py
# A program using an indefinite loop to get the average of a n numbers.

def main():

    total = 0.0
    count = 0
    moredata = "yes"
    while moredata[0] == "y":
        x = float(input("Enter a number: "))
        total = total + x
        count = count + 1
        moredata = input("Do you have more numbers? (yes/no) ")
    print("\nThe average of the numbers is", total / count)
    
main()
