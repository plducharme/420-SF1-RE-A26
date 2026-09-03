# Opérateurs en place "in place"
a = 6
a += 4  # équivaut à a = a + 4
print(a)

b = 8
b //= 6  # équivaut b = b // 6
print(b)

# ceci existe pour tous les opérateurs de bases
c = 9
d = 12

d **= c  # équivaut d = d ** c
print(d)

# Exemple d'utilisation
compteur = 1
for i in range(9):
    compteur += 1
print(compteur)
