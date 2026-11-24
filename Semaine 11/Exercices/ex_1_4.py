phrase = input("Phrase : ")
phrase = phrase.lower()
# Pour enlever les espace, on remplace les espaces par un caractère vide ""
phrase = phrase.replace(" ", "")
if phrase == phrase[::-1]:
    print("Palindrome magique !")
