# Définition d'ensembles
fruits = {'banane', 'pomme', 'poire', 'bleuet', 'fraise'}

panier = {'banane', 'bleuet', 'lait', 'pomme', 'beurre'}

garde_manger = set(['banane', 'poire'])

# Définition en compréhension, extra
frigidaire = {x for x in panier if x not in garde_manger}
print(frigidaire)

# Éléments dans panier moins ceux dans fruits (différence)
print(panier - fruits)
print(panier.difference(fruits))

# Éléments dans fruits moins ceux dans panier
print(fruits - panier)

# items dans fruits ou panier (union)
print(panier | fruits),
print(panier.union(fruits))

# items dans fruits et panier (intersection)
print(panier & fruits)
print(panier.intersection(fruits))

# items exclusivement dans le panier ou dans fruits (XOR)
print(panier ^ fruits)
print(panier.symmetric_difference(fruits))

# union entre fruits et panier (|)
print(fruits.union(panier))
# union entre fruits et itérable
print(fruits.union(('mure', 'pomme', 'mangue')))
