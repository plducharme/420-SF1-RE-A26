import math


# Une fonction peut avoir 0 ou plusieurs paramètres
# ex sans paramètre
def bonjour():
    print("Bonjour le monde!")


for i in range(2):
    bonjour()


# exemple avec 2 paramètres
def pythagore(base, hauteur):
    hypothenuse = math.sqrt(base ** 2 + hauteur ** 2)
    return hypothenuse


resultat = pythagore(7, 8)
print(resultat)
print(pythagore(3, 4))
print(pythagore(7, 14))


# Extra, il est possible de définir des fonctions qui prennent un nombre illimité de paramètres
# On utilise * devant le paramètre
def somme(*args):
    total = 0
    for i in args:
        total += i
    return total


print(somme(4, 5, 5, 8, 9, 12))
