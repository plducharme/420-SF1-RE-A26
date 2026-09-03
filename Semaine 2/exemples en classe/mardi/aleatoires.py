import random

# Choisir un élément au hasard dans une liste
liste = ["Patate", "Tomate", "Raisin", "Orange"]
print(random.choice(liste))

# Pour une valeur aléatoire entre 0 et 1
print(random.random())

# Pour un entier aléatoire entre 2 bornes
print(random.randint(32, 99))

# Pour recréer de l'aléatoire
random.seed(42)
print(random.randint(0, 10))
print(random.randint(0, 10))

