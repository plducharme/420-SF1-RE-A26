# Pour utiliser la bibliothèque math incluse avec python :
import math

factoriel_de_5 = math.factorial(5)
print(factoriel_de_5)

angle_degres = 30.0
angle_en_radians = math.radians(angle_degres)
sinus = math.sin(angle_en_radians)
print("sin(30deg): ", sinus)

base = 4
hauteur = 3
hypo = math.sqrt(base**2 + hauteur**2)
print("Hypothénuse de a = 4, b = 3: ", hypo)

print("hypo: ", math.hypot(base, hauteur))

print(math.floor(10/3))
print(10 // 3)

# puissance
print(2**6)
print(math.pow(2, 6))
print(pow(2, 6))

# Somme des éléments d'une liste
liste_nombres = [3, 5, 7, 12, 42, 99]
print(math.fsum(liste_nombres))

# Somme des impaires
liste_impairs = [i for i in range(1, 14, 2)]
print("Liste impairs: ", liste_impairs)
print("Somme impairs: ", math.fsum(liste_impairs))


