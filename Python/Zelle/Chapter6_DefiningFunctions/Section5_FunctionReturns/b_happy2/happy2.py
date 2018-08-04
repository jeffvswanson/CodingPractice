# happy2.py

def happy():
    return "Happy Birthday to you!"

def verseFor(person):
    lyrics = happy()*2 + "Happy Birthday, dear " + person + ".\n" + happy()
    return lyrics

def main():
    for person in ["Fred", "Lucy", "Elmer"]:
        print(verseFor(person))

main()
