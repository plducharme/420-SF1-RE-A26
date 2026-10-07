
mot = input("Entrez le mot: ")
sequence_lettres = input("Entrez la séquence de lettres: ")


def inverser_chaine(chaine: str) -> str:
    inverse = ""

    for caractere in chaine:
        inverse = caractere + inverse

    return inverse


if mot.find(sequence_lettres) != -1 or mot.find(inverser_chaine(sequence_lettres)) != -1:
    print(f"le mot '{mot}' est composable à partir de {sequence_lettres}")
else:
    print(f"le mot '{mot}' n'est pas composable à partir de {sequence_lettres}")