# On considère les nombres pairs entre 600 et 700
for nb in range(600, 701, 2):

    nb_str = str(nb)
    premier_chiffre = int(nb_str[0])
    deuxieme_chiffre = int(nb_str[1])
    troisieme_chiffre = int(nb_str[2])

    # On vérifie qu'un des chiffres est 3
    if premier_chiffre == 3 or deuxieme_chiffre == 3 or troisieme_chiffre == 3:
        # On vérifie si la somme des 3 chiffres est 11
        if premier_chiffre + deuxieme_chiffre + troisieme_chiffre == 11:
            # On a trouvé la réponse, on sort de la boucle
            print(f"Le nombre est {nb}")
            break


