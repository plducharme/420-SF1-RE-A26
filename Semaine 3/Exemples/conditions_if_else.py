
a = int(input("Entrez un nombre:\t"))

# si la condition est vrai, tout ce qui est indenté après les ":" sera exécuté
# si la condition est fausse, le bloc else sera exécuté
if a >= 0:
    print("Le nombre est positif")
    print("Deuxième instruction si positif")

    # L'indentation compte, même s'il y a une ligne vide
    print("Toujours dans le bloc if")
else:
    print("Le nombre est négatif")
    print("Deuxième instruction si négatif")

print("Fin du programme!")
