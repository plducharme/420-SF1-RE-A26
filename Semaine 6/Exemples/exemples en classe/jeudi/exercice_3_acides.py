

def valider_chaine(chaine: str) -> bool:

    for c in chaine:
        match c:
            case "A":
                continue
            case "R":
                continue
            case "W":
                continue
            case "G":
                continue
            case _:
                return False

    return True


def afficher_frequence(acide: str, chaine: str):
    print(f"% acide {acide} est {chaine.count(acide) / len(chaine) * 100}")


chaine = input("Veuillez entrer une chaîne: ")

if not valider_chaine(chaine):
    print("Chaîne invalide")
else:
    afficher_frequence("A", chaine)
    afficher_frequence("R", chaine)
    afficher_frequence("W", chaine)
    afficher_frequence("G", chaine)
