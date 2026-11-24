heros = {
    'nom': 'Aria',
    'classe': 'magicienne',
    'niveau': 1,
    'stats': {'force': 4, 'magie': 9, 'agilité': 6}
}


def afficher_personnage(personnage: dict) -> None:
    print(f"{personnage["nom"]}, {personnage["classe"]} (niveau {personnage["niveau"]})")
    stats: dict = personnage["stats"]
    for cle, valeur in stats.items():
        print(f"\t{cle} : {valeur}")


afficher_personnage(heros)


def monter_niveau(personnage: dict):
    personnage["niveau"] += 1
    stats = personnage["stats"]
    for stat in stats.keys():
        stats[stat] += 2


monter_niveau(heros)
afficher_personnage(heros)
