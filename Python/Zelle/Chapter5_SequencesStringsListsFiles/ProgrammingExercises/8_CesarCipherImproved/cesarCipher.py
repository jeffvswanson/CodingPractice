# cesarCipher2.py
# A program to create a substitution cipher.
"""One problem with problem 7 is that it does not deal with the case when we
"drop off the end" of the alphabet. A true Caesar cipher does the shifting in a
circular fashion where the next character oafter "z" is "a." Modify your
solution to the previous problem to make it circular. You may assume that the
input consists only of letters and spaces. Hint: Make a string containing all
the characters of your alphabet and use positions in this string as your code.
You do not have to shift "z" into "a"; just make sure that you use a circular
shift over the entire sequence of characters in your alphabet string."""

def main():

    print("This program converts a message to a substitution cipher")
    print("with a key value chosen by the user.\n")

    # Get the message to encode.
    message = print("Please enter the message you want to encode")
    message = input("(letters and spaces only): ")
    message = message.lower()
    key = int(input("Please enter the key number: ")) 

    alphabet = "abcdefghijklmnopqrstuvwxyz "
    alphabetList = list(alphabet)
    
    # Loop through the string and build the ciphered message
    # z will show up as a space " " when printed and a space as "a" when
    # shifted one.    
    chars = []
    for ch in message:
##        print(ch)
##        print(alphabetList.index(ch))
##        print(alphabetList.index(ch) + key)
##        print((alphabetList.index(ch) + key) % (len(alphabetList)))
##        print(alphabetList[(alphabetList.index(ch) + key) \
##                           % (len(alphabetList))])
        chars.append(alphabetList[(alphabetList.index(ch) + key) \
                                  % (len(alphabetList))])

    cipher = "".join(chars)
    print("\nThe encoded message is:", cipher)

main()
