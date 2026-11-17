import csv

with open('Periodic Table of Elements.csv', 'r', encoding='utf8') as fichier_csv:
    liste_elements = csv.DictReader(fichier_csv)
