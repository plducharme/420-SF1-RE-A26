import random


def choix_ordi():
    return random.choice(["roche", "papier", "ciseaux"])


# retourne 0 si nul, 1 si gagné, 2 si perdu
def resultat(choix_joueur: str, choix_ordi: str) -> int:
    match choix_joueur:
        case "roche":
            if choix_ordi == "roche":
                return 0
            elif choix_ordi == "papier":
                return 2
            else:
                return 1
        case "papier":
            if choix_ordi == "roche":
                return 1
            elif choix_ordi == "papier":
                return 0
            else:
                return 2
        case "ciseaux":
            if choix_ordi == "roche":
                return 2
            elif choix_ordi == "papier":
                return 1
            else:
                return 0
        case _:
            return 0


def jeu():
    while True:
        choix_joueur = input("[r]oche, [p]apier, [c]iseaux")
        choix_cpu = choix_ordi()
        if choix_joueur == "r":
            r = resultat("roche", choix_cpu)
        elif choix_joueur == "p":
            r = resultat("papier", choix_cpu)
        elif choix_joueur == "c":
            r = resultat("ciseaux", choix_cpu)
        else:
            print("Choix invalide! \u274C")
            continue

        if r == 0:
            print(f"CPU: {choix_cpu}, match nul!")
        elif r == 1:
            print(f"CPU: {choix_cpu}, vous avez gagné!")
        else:
            print(f"CPU: {choix_cpu}, vous avez perdu!")


if __name__ == "__main__":
    jeu()
