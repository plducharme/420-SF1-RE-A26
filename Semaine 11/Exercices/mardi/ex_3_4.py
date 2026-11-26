heros = {
    'nom': 'Aria',
    'classe': 'magicienne',
    'niveau': 1,
    'stats': {'force': 4, 'magie': 9, 'agilité': 6}
}


def afficher_personnage(perso: dict):
    print(f"{perso["nom"]}, {perso["classe"]} (niveau {perso["niveau"]})")
    for nom_stat, valeur in perso["stats"].items():
        print(f"\t{nom_stat} : {valeur}")


afficher_personnage(heros)

heros["niveau"] += 1
for stat in heros["stats"].keys():
    heros["stats"][stat] += 2

afficher_personnage(heros)
