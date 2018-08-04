# dateConvert2Improved.py
# Converts day month and year numbers into two date formats
"""As discussed in the chapter, string formatting could be used to simplify the
dateconvert2.py program. Go back and redo this program making use of the string-
formatting method."""

def main():

    # get the day month and year
    day, month, year = int(input("Please enter day, month, \
and year numbers: "))

    date1 = "{0}/{1}/{2}".format(month, day, year)

    months = ["January", "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December"]
    monthStr = months[month - 1]

    date2 = "{0} {1}, {2}".format(monthStr, day, year)
    
    print("The date is: {0} or {1}.".format(date1, date2))
    
main()
