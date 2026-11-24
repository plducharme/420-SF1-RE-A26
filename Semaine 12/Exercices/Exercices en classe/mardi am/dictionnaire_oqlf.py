import csv

# Ouverture de fichier
with open("termes_officialises_2026-01-14.csv", mode="r", encoding="utf8") as fichier:
    dict_reader = csv.DictReader(fichier)

    # liste des domaines
    domaines = []

    for ligne_dict in dict_reader:
        domaines.append(ligne_dict["Domaines"])
    # utilise la liste de domaines pour créer un ensemble sans doublons
    domaines_ensemble = set(domaines)
    # On utilise l'ensemble pour recréer une liste sans doublons
    domaines = list(domaines_ensemble)

    print(f"Nombre d'éléments uniques de domaines: {len(domaines)}")


