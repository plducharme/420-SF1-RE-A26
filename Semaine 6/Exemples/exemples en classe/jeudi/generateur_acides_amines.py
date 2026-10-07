import random


def generer_data(longueur: int):
    acide_ok = ["A", "R", "W", "G"]
    acide_erreur = ["A", "R", "T", "G"]
    with open("chaine-ok.txt", "w", encoding="utf8") as fichier:
        for i in range(longueur):
            fichier.write(random.choice(acide_ok))

    with open("chaine-erreur.txt", "w", encoding="utf8") as fichier:
        for i in range(longueur):
            fichier.write(random.choice(acide_erreur))


def charger_data(ok: bool) -> str:

    if ok:
        nom_fichier = "chaine-ok.txt"
    else:
        nom_fichier = "chaine-erreur.txt"

    with open(nom_fichier, "r", encoding="utf8") as fichier:
        return fichier.read()


if __name__ == "__main__":
    generer_data(1024)
