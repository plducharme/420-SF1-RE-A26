dict_fra_elfique = {"ami": "mellon", "lumière": "ithil", "magicien": "Istar", "salut": "aia", "premier": "inga"}

phrase = input("Phrase : ")
liste_mots = phrase.split()
traduction = []
for mot in liste_mots:
    if mot in dict_fra_elfique:
        traduction.append(dict_fra_elfique[mot])
    else:
        traduction.append(f"[{mot}]")

print(" ".join(traduction))


