# happy.py
# A program that prints the lyrics to "Happy Birthday"

def happy():
    print("Happy Birthday to you!")

def sing(person):
    happy()
    happy()
    print("Happy birthday, dear", person + ".")
    happy()

def main():
    sing("Fred")
    print()
    sing("Lucy")
    print()
    sing("Elmer")

main()
