# Opérateurs "en place"
a = 3
b = 5
a += b  # équivaut à a = a + b

compteur = 0
for i in range(12):
    compteur += 1  # équivaut à compteur = compteur + 1
print(compteur)

somme_exponentielle = 2
for i in range(10):
    somme_exponentielle **= 2
print(somme_exponentielle)


