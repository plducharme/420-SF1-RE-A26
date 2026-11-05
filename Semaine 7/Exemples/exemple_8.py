voyelles = ["a", "e", "i", "o", "u", "y"]

for lettre in enumerate(voyelles):
    print(lettre)
# Une liste est un itérable... on peut boucler dessus
# enumerate(itérable) retourne un tuple contenant (index de l'itération, l'élément à l'index de l'itération
# de l'itérable).
# i.e. (0, "a") puis (1, "e") puis (2, "i"), etc
for index, lettre in enumerate(voyelles):
    print(f"La voyelle à l'itération {index} est {lettre}")

# Faire attention, enumerate retourne l'index de l'itération et non de l'élément
liste_entiers = list(range(10))
print(liste_entiers)

for index, entier in enumerate(liste_entiers[::2]):
    print(f"index de l'itération: {index} entier: {entier}")

