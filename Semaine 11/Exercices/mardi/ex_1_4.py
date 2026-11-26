phrase = input("Phrase : ")
phrase = phrase.replace(" ", "")
phrase = phrase.lower()

if phrase[::-1] == phrase:
    print("Palindrome magique !")
