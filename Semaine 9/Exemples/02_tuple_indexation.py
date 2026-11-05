mes_coords_depart = (3, 4, 5)
mes_coords_arrivee = (23, 42, 666)

# on peut accéder à un élément en utilisant son index
print(mes_coords_depart[0])  # affiche 3
print(mes_coords_depart[1])  # affiche 4

# On peut utiliser l'opérateur d'indexation pour retourner une partie du tuple [début:fin non inclus: pas]
print(mes_coords_arrivee[0:2])

# Comme pour les listes et les str, l'opérateur d'indexation peut avoir des valeurs par défaut
print(mes_coords_arrivee[:2])  # de 0 à 2 non inclus -> (23, 42)
print(mes_coords_arrivee[1:])  # de 1 à la fin (42, 666)

# Ne pas oublier, le "slicing" (i.e. opérateur d'indexation [début:fin non incluse:pas]) retourne une copie contenant le
# slicing demandé, donc un tuple
tuple_sans_premier = mes_coords_arrivee[1:]
print(type(tuple_sans_premier))








