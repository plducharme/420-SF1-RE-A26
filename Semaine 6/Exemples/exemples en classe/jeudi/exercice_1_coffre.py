for nombre in range(600, 701, 2):

    nombre_str = str(nombre)
    chiffre_1 = nombre_str[0]
    chiffre_2 = nombre_str[1]
    chiffre_3 = nombre_str[2]

    if nombre_str.find("3") == -1:
        continue
    elif int(chiffre_1) + int(chiffre_2) + int(chiffre_3) != 11:
        continue
    else:
        print(f"La combinaison est {nombre}")
        break


# Autre version
for nombre in range(600, 701, 2):

    nombre_str = str(nombre)
    chiffre_1 = nombre_str[0]
    chiffre_2 = nombre_str[1]
    chiffre_3 = nombre_str[2]

    if "3" not in nombre_str:
        continue
    elif int(chiffre_1) + int(chiffre_2) + int(chiffre_3) != 11:
        continue
    else:
        print(f"La combinaison est {nombre}")
        break
