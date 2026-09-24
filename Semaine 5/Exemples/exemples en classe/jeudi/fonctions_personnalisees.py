import math

# fonctions à 1 paramètre
def salutations(nom):
    print(f"Bonjour {nom}!")


salutations("Pier Luc")
salutations("Mustapha")


def citation():
    print("Connais-toi toi-même!")


# On doit mettre les parenthèses même s'il n'y a aucun argument
citation()


# fonctions à plusieurs paramètres
def pythagore(base, hauteur):
    hypothenuse = math.sqrt(base**2 + hauteur**2)
    print(f"L'hypothénuse d'un triangle de base {base} et hauteur {hauteur} est de {hypothenuse}")


pythagore(3, 4)


# *args permet de spécifier un nombre illimité de paramètres
def somme(*args):
    total = 0
    for nb in args:
        total += nb
    print(f"La somme est de {total}")


somme(42, 5.0, 6, -5, 2**3)



