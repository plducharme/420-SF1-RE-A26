import random

liste_choix = ["Premier", "Deuxième", "Troisième", "Autre", "Patate"]
print(f"liste originale: {liste_choix}")

# random.choice() retourne un élément au hasard d'une liste
print(random.choice(liste_choix))
print(random.choice(liste_choix))
print(random.choice(liste_choix))
print(random.choice(liste_choix))
print(random.choice(liste_choix))

# random.shuffle() mélange aléatoirement les éléments d'une liste. Ceci la modifie.
random.shuffle(liste_choix)

print(f"liste après shuffle(): {liste_choix}")
