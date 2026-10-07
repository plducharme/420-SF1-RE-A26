def saisie_nombres(valider_zero=False):
    nb1 = int(input("Entrez un premier nombre: "))

    while True:
        nb2 = int(input("Entrez un deuxième nombre: "))

        if valider_zero and nb2 == 0:
            print("Le deuxième nombre ne peut pas être 0")
            continue
        break
    return nb1, nb2


while True:

    choix = int(input("Choisissez une option:\n\t[1] Addition\n\t[2] Soustraction\n\t[3] Multiplication\n\t[4] "
                      "Division\n\t[5] Puissance\nChoix?: "))

    match choix:

        case 1:
            nb1, nb2 = saisie_nombres()
            print(f"Le résultat de l'addition de {nb1} et {nb2} = {nb1 + nb2}")
        case 2:
            nb1, nb2 = saisie_nombres()
            print(f"Le résultat de la soustraction de {nb1} et {nb2} = {nb1 - nb2}")
        case 3:
            nb1, nb2 = saisie_nombres()
            print(f"Le résultat de la multiplication de {nb1} et {nb2} = {nb1 * nb2}")
        case 4:
            nb1, nb2 = saisie_nombres(True)
            print(f"Le résultat de la division de {nb1} par {nb2} = {nb1 / nb2}")
        case 5:
            nb1, nb2 = saisie_nombres()
            print(f"Le résultat de {nb1} à la puissance {nb2} = {nb1 ** nb2}")
        case _:
            print("Choix invalide")
