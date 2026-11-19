bestiaire = {'gobelin': 10, 'troll': 50, 'dragon': 200}
print(bestiaire["troll"])
bestiaire["fantome"] = 30
# équivalent de bestiaire["dragon"] = bestiaire["dragon"] // 2
bestiaire["dragon"] //= 2
del bestiaire["gobelin"]
for monstre, pdv in bestiaire.items():
    print(f"{monstre} : {pdv}")

