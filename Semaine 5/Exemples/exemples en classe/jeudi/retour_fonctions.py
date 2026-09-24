import math


# une fonction peut retourner une ou plusieurs valeurs
def pythagore(base, hauteur):
    hypo = math.sqrt(math.pow(base, 2) + math.pow(hauteur, 2))
    return hypo


# Le retour d'une fonction peut être assigné à une variable
h = pythagore(3, 4)
print(h)


# Le retour d'une fonction peut aussi être passé en paramètre d'une autre fonction
print(pythagore(5, 6))


# Pour calculer le sinus d'un angle de 30 degrés
angle_en_degres = 30
angle_en_radians = math.radians(angle_en_degres)
sinus = math.sin(angle_en_radians)
print(sinus)

