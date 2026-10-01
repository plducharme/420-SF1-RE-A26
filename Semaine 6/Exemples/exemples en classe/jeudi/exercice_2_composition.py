mot = input("Entrez un mot: ")
sequence = input("Entrez la séquence recherchée: ")


def inverser_chaine(chaine: str) -> str:
    chaine_inverse = ""

    for lettre in chaine:
        chaine_inverse = lettre + chaine_inverse
    return chaine_inverse


# on peut utiliser le slicing pour inverser la chaîne. [::-1] du début à la fin avec un pas de -1.
# Petit chaine[-1] est le dernier caractère de la chaîne, -2, l'avant-dernier, etc
def inverser_chaine_v2(chaine: str) -> str:
    return chaine[::-1]


if sequence.find(mot) != -1:
    print(f"{mot} est composable à partir de {sequence}")
elif sequence.find(inverser_chaine_v2(mot)) != -1:
    print(f"{mot} est composable à partir de {sequence}")
else:
    print(f"{mot} n'est PAS composable à partir de {sequence}")

