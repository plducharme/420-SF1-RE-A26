import random

liste_planetes = ["Mercure", "Vénus", "Terre", "Mars", "Jupiter", "Saturne", "Uranus", "Neptune"]

planete_mystere = random.choice(liste_planetes)

while True:

    choix_planete = input("Entrez la planète : ")

    if choix_planete == planete_mystere:
        print("Vous avez découvert la planète mystère!")
        break
    else:
        index_choix = liste_planetes.index(choix_planete)
        index_planete_mystere = liste_planetes.index(planete_mystere)

        if index_choix < index_planete_mystere:
            print("Plus loin du Soleil")
        else:
            print("Plus près du Soleil")

