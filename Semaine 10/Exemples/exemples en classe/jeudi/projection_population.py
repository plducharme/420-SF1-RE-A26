import csv

with open("births-and-deaths-projected-to-2100.csv", "r") as fichier_csv:

    liste_entrees = csv.DictReader(fichier_csv)
    total_morts_1980 = 0
    total_naissances_1980 = 0
    total_naissances_canada = 0

    for dict_ligne in liste_entrees:
        if dict_ligne["Pays"] == "World":
            continue
        # calculer le nombre de morts en 1980
        # s'assurer que la valeur ne soit pas un str vide avant de la convertir en int
        # calculer ler nombre de naissances en 1980
        # s'assurer que la valeur ne soit pas un str vide avant de la convertir en int
        if dict_ligne["Year"] == "1980" and dict_ligne["Morts"] != "" and dict_ligne["Naissances"] != "":
            total_morts_1980 += float(dict_ligne["Morts"])
            total_naissances_1980 += float(dict_ligne["Naissances"])

        # calculer le nombre total de naissances au Canada de 1950 à 2000
        if dict_ligne["Pays"] == "Canada" and 1950 <= int(dict_ligne["Year"]) <= 2000:
            total_naissances_canada += int(dict_ligne["Naissances"])

print(f"1980: Naissances: {total_naissances_1980} Morts: {total_morts_1980} diff: {total_naissances_1980 - total_morts_1980}")
print(f"Naissances Canada de 1950 à 2000: {total_naissances_canada}")
    # faire un graphique des naissances au Canada de 1950 à 1975

