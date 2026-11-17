def somme(*entiers):
    print('Arguments: ' + str(entiers))
    total = 0
    for x in entiers:
        total += x

    return total


print(somme(5, 9, 12, 2))
print(somme(1, 42, 98, 156, -7, 65))


def afficher_arguments(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k + ':\t' + v)


afficher_arguments(nom='Ducharme', prenom='Pier Luc', grandeur='6 pieds')

# Le unpacking permet aussi de:
boule1, boule2, boule3 = ("b1", "b2", "b3")
print(boule1)
print(boule2)
print(boule3)
