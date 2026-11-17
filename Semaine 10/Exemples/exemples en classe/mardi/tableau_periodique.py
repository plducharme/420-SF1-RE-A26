import csv
import pandas as pd
import numpy as np

# Lecture d'un csv pour obtenir une liste de dictionnaires (un dictionnaire par ligne du fichier)
# La première ligne du fichier contient le nom des entêtes (qui seront les clés des dictionnaires)
with open("Periodic Table of Elements.csv", "r", encoding="utf8") as fichier_csv:
    liste_elements = csv.DictReader(fichier_csv)

    total_masse_atomique = 0
    nb_elements = 0
    solides = []
    for element in liste_elements:
        total_masse_atomique += float(element["AtomicMass"])
        nb_elements += 1
        if element["Phase"] == "solid":
            solides.append(element["Element"])
    print(f"Moyenne des masses atomiques: {total_masse_atomique/nb_elements}")
    print(f"Liste des éléments solides: {solides}")


####
dataframe = pd.read_csv("Periodic Table of Elements.csv")
dataframe.info()
print(f"moyenne des masses atomiques: {np.mean(dataframe["AtomicMass"])}")
print(f"moyenne des masses atomiques: {dataframe["AtomicMass"].mean()}")
print(f"Médiane des masses atomiques: {dataframe["AtomicMass"].median()}")












