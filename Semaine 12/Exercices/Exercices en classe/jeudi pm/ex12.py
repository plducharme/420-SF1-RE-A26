echantillons = []

while len(echantillons) < 10:
    echantillons.append(input("Échantillons collectés: "))

print(f"Nombre d'éléments uniques: {len(set(echantillons))}" )