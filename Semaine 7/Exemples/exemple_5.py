# list(séquence) génère une liste à partir de la séquence
# range(début, fin non incluse, pas) génère une séquence
liste_10 = list(range(10))

print(liste_10)
print(liste_10[5])  # affiche 5

liste_5_13 = list(range(5, 13))
print(liste_5_13)
# range(debut, fin exclus, pas)
print(list(range(6, 15, 3)))

# Ne pas oublier que les str sont aussi des séquences. Générer une liste à partir d'une str, va générer une liste où
# chaque élément sera un caractère.
liste_str = list("Vive le python!")
print(liste_str)

# Si on ne spécifie pas de séquence, une liste vide est créée
liste_vide = list()
# même chose que faire
liste_vide_2 = []
print(liste_vide, liste_vide_2, sep=" == ")
print(liste_vide == liste_vide_2)
