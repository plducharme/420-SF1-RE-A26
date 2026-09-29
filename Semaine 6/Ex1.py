for nombre in range(600, 701, 2):
    total_chiffres = 0

    for i in str(nombre):
        total_chiffres += int(i)

    if '3' in str(nombre) and total_chiffres == 11:
        print('Le nombre est', nombre)
        break
