# Il existe des fonctions prédéfinies incluses avec python
# https://docs.python.org/3/library/functions.html

# En plus de celles-ci, on peut importer des bibliothèques incluses avec python
import math

# plancher de la division
print(8 // 3)
print(math.floor(8/3))

# 2 ** 3
print(math.pow(2, 3))

# racine carrée de 9
print(9**0.5)
print(math.sqrt(9))


# Trigo, attention les angles sont en radians
# Sinu de 30 degrés
sinus = math.sin(math.radians(30))
print(sinus)

# PI
print(math.pi)

# Pseudo aléatoire
# https://docs.python.org/fr/3.14/library/random.html#module-random
import random

print(random.randint(50, 100))
print(random.randint(50, 100))
print(random.randint(50, 100))

# valeur aléatoire entre 0 et 1
print(random.random())

# Choisir un élément au hasard dans une liste
liste = [5, 42, 66, 89, 12]
print("Choice: ", random.choice(liste))

liste2 = ["patate", "poire", "pomme", "raisin"]
print(random.choice(liste2))

# Mélanger une liste
liste3 = [1, 2, 3, 4, 5]
random.shuffle(liste3)
print("Après shuffle(): ", liste3)


# Comment reproduire de l'aléatoire
# On utilise une graine (seed)
random.seed(42)
print(random.randint(0, 10))
print(random.randint(0, 10))
print(random.randint(0, 10))



