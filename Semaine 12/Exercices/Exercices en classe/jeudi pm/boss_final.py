import random

nombre = random.randint(1, 50)
nb_essais = 0
while True:

    nb_joueur = int(input("Entrez un nombre: "))
    nb_essais += 1
    if nb_joueur == nombre:
        print("Bravo!")
        break
    elif nb_joueur < nombre:
        print("plus haut")
    else:
        print("plus bas")

print(f"Vous avez fait {nb_essais} essais")
