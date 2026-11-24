explorateur1 = {"zorg", "blip", "xelon"}
explorateur2 = {"xelon", "nova", "krill"}

# intersection
print(f"Espèces découvertes par les deux: {explorateur1 & explorateur2}")
print(f"Espèces découvertes par les deux: {explorateur1.intersection(explorateur2)}")
# union
print(f"Espèces découvertes: {explorateur1 | explorateur2}")
print(f"Espèces découvertes: {explorateur1.union(explorateur2)}")

# différence symétrique
print(f"Espèces découvertes par un ou par l'autre, mais pas les deux: {explorateur1 ^ explorateur2}")
print(f"Espèces découvertes par un ou par l'autre, mais pas les deux: {explorateur1.symmetric_difference(explorateur2)}")
