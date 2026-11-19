phrase = input("Phrase : ")
print(phrase.upper())
nb_voyelles = 0
phrase_chuchotee = ""
for lettre in phrase:
    if lettre in "aeiouy":
        nb_voyelles += 1
        phrase_chuchotee = phrase_chuchotee + "*"
    else:
        phrase_chuchotee = phrase_chuchotee + lettre
print(f"Voyelles : {nb_voyelles}")
print(phrase_chuchotee)
