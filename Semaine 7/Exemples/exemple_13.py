import random

# permet de générer toujours le même pseudo-aléatoire
random.seed(42)

liste_nombres = []
# on se génère une lsite avec des entiers aléatoires
for i in range(10):
    liste_nombres.append(random.randint(0, 100))

print(liste_nombres)

# sort() trie la liste en la modifiant
liste_nombres.sort()
print(liste_nombres)

# sorted(séquence) trie la liste sans la modifier et retourne une nouvelle (triée)
liste_nombres_2 = [42, 66, 3, -4, 81]
liste_triee = sorted(liste_nombres_2)
print(liste_nombres_2)
print(liste_triee)

# on peut triee en ordre décroissant avec le paramètre reverse=True
liste_decroissante = sorted(liste_nombres_2, reverse=True)
print(liste_decroissante)

# .sort(reverse=True) est aussi possible
liste_nombres_3 = [5, 96, -1, 42, 45, 77]
liste_nombres_3.sort(reverse=True)
print(liste_nombres_3)


