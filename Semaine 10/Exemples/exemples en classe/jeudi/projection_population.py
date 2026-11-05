import csv

with open("births-and-deaths-projected-to-2100.csv", "r") as fichier_csv:

    liste_entrees = csv.DictReader(fichier_csv)

    for dict_ligne in liste_entrees:
        if dict_ligne["World"]:
            continue
        # calculer le nombre de morts en 1980
        # s'assurer que la valeur ne soit pas un str vide avant de la convertir en int

        # calculer ler nombre de naissances en 1980
        # s'assurer que la valeur ne soit pas un str vide avant de la convertir en int

        # calculer le nombre total de naissances au Canada entre 1950 et 2000



