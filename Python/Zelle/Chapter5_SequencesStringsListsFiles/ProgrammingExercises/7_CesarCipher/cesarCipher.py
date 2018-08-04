# cesarCipher2.py
# A program to create a substitution cipher.
"""A Caesar cipher is a simple substitution cipher based on the idea of shifting
each letter of the plaintext message a fixed number (called the key) of
positions in the alphabet. For example, if the key value is 2, the word
"Sourpuss" would be encodes "Uqwtrwuu." The original message can be recovered by
"reencoding" it using the negative of the key.

Write a program that can encode and decode Caesar ciphers. The input to the
program will be a string of plaintext and the value of the key. The output will
be an encoded message where each character in the original message is replaced
by shifting it ey character in the Unicode character set. For ecample, if ch is
a character in the string and key is the amount to shift, then the character
that replaces ch can be calculated as: chr(ord(ch) + key)."""

def main():

    print("This program converts a message to a substitution cipher")
    print("with a key value chosen by the user.\n")

    # Get the message to encode.
    message = print("Please enter the message you want to encode")
    message = input("(letters and spaces only): ")
    message = message.lower()
    key = eval(input("Please enter the key number: ")) 

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
