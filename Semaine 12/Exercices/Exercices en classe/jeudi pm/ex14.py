planetes = {
    "Mercure": 58,
    "Vénus": 108,
    "Terre": 150,
    "Mars": 228
}

nom_planete = input("Donnez le nom d'une planète: ")
print(f"{planetes.get(nom_planete, "planète inconnue!")}")

if nom_planete in planetes:
    print(planetes[nom_planete])
else:
    print("planète inconnue!")


