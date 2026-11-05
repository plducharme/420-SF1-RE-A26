import random


def partie_rpc(choix_joueur: str) -> tuple[int, str]:
    # retourne 0 si perdu, 1, si gagné, 2 si nulle
    choix_ordi = random.choice(["roche", "papier", "ciseaux"])

    if choix_joueur == "roche":
        if choix_ordi == "roche":
            return 2, choix_ordi
        elif choix_ordi == "papier":
            return 0, choix_ordi
        else:
            return 1, choix_ordi
    elif choix_joueur == "papier":
        if choix_ordi == "roche":
            return 1, choix_ordi
        elif choix_ordi == "papier":
            return 2, choix_ordi
        else:
            return 0, choix_ordi
    else:
        if choix_ordi == "roche":
            return 0, choix_ordi
        elif choix_ordi == "papier":
            return 1, choix_ordi
        else:
            return 2, choix_ordi


def jeu():
    while True:
        input_joueur = input("Choisissez [r]oche [p]apier ou [c]iseaux")
        resultat = 0
        choix_ordi = ""
        match input_joueur:
            case "r":
                resultat, choix_ordi = partie_rpc("roche")
            case "p":
                resultat, choix_ordi = partie_rpc("papier")
            case "c":
                resultat, choix_ordi = partie_rpc("ciseaux")
            case _:
                print("Choix invalide")
                continue

        print("CPU a choisi: " + choix_ordi)
        if resultat == 0:
            print("Vous avez perdu")
        elif resultat == 1:
            print("Vous avez gagné")
        else:
            print("Partie nulle")


if __name__ == "__main__":
    jeu()
