import math

# print() affiche les valeurs passées en paramètres
print("Bonjour!")

# input(str) affiche la str et retourne l'entrée de l'usager
entree = input("Entrez une phrase: ")

# abs(valeur) retourne la valeur absolue
print(abs(-5))

# sum(iterable, debut) retourne la somme des éléments de l'itérable en ajoutant "debut" (optionnel) au début de
# l'itérable
liste_valeurs = [3, 6, 88, 42, -5, 7]
print(sum(liste_valeurs, 5))

# On a déjà vu les fonctions pour transformer les types: int(), float(), str(), hex(), oct(), bool(), bin(), chr()
print(int(5.6))

# len(iterable) retourne la longueur (nombre d'éléments) d'un itérable
liste_matieres = ["chimie", "physique", "informatique", "mathématiques"]
print(len(liste_matieres))
citation = 'L\'ordinateur a de la mémoire, mais aucun souvenir.'
print(len(citation))

# all(iterable) retourne True si toutes les conditions dans l'itérable sont vraies
liste_conditions = [5 < 6, True, 42 == 42]
print(all(liste_conditions))

# any(iterable) retourne True si au moins une des conditions de l'itérable est vraie
liste_conditions_2 = [6 < -1, False, 33 == 42, True]
print(any(liste_conditions_2))

liste_numerique = [2**64, 1024, 666, 42, -1]
# min(iterable) retourne la valeur minimum de l'itérable
print(min(liste_numerique))

# max() retourne la valeur maximale de l'itérable
print(max(liste_numerique))

# range(debut(optionnel), fin non-incluse, pas(optionnel)) génère une séquence itérable de debut à fin non-incluse
# en incrémentant du "pas"
for i in range(4, 20, 2):
    print(i, end=" ")
print()

# round(valeur, digits) arrondi la valeur au nombre de "digits" (décimales)
print(round(math.pi, 4))

