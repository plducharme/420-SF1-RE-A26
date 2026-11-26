import string

phrase = input("Phrase : ")
alphabet = set(string.ascii_lowercase)
phrase = phrase.replace(" ", "")
phrase_ensemble = set(phrase)
manquantes = alphabet - phrase_ensemble

if not manquantes:
    print("C'est un pangramme !")
else:
    print(f"Pas un pangramme. Lettres manquantes : {" ".join(sorted(manquantes))}")