# exemple 2
liste_fruits = ["fraises", "framboises", "pommes", "bleuets"]
liste_premiers = [2, 3, 5, 7, 11, 13]

# affiche le premier élément de la liste des premiers
print(liste_premiers[0])

# affiche le deuxième élément de la liste de fruits
print(liste_fruits[1])

# affiche la première lettre du troisième fruit
# liste_fruits[2] retourne "pommes" et "pommes"[0] retourne "p"
print(liste_fruits[2][0])

# Ceci causera une erreur, car les str sont immuables (non-modifiables)
liste_fruits[2][0] = "t"

