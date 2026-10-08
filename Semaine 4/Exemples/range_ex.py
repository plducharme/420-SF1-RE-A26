# il existe trois "versions" de la méthode built-in range(debut inclus, fin non-incluse, pas)
# Dans les faits, c'est la même fonction, mais avec des paramètres optionnels
# Le "pas" est de combien la séquence incrémente (1, si non spécifié)
# range(fin non incluse) génère une séquence de 0 à fin-1
for i in range(10):
    print(i, end=" ")
print()

# range(debut inclus, fin non incluse)
for i in range(1, 11):
    print(i, end=" ")
print()

# range(debut inclus, fin non-incluse, pas) génère une séquence de debut à fin non incluse en incrémentant de "pas"
# à chaque itération
for i in range(2, 20, 2):
    print(i, end=" ")
print()

# Cette dernière version permet aussi de faire des séquences qui diminuent
for i in range(15, 1, -1):
    print(i, end=" ")
print()


for i in range(10):
    # pas obligé d'utilisé la variable i déclarée
    print("Exécuté", end=" ")

# La façon la plus élégante de faire une boucle for qui n'utilise pas la variable
for _ in range(10):
    print("Exécuté!", end=" ")

    