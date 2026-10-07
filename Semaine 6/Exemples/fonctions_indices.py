import math
# il est possible de donner des indices à python (et Pycharm) sur le type des variables et paramètres


# Pour les fonctions
# Dans cet exemple, j'indique que le premier paramètre devrait être une str et que le deuxième devrait être un float
# La flèche (tiret plus grand) -> indique le type de retour attendu
def afficher_nombre(nom: str, nombre: float) -> float:
    print(f"Bonjour {nom}! Votre nombre est {nombre}")
    return nombre**2


# Ceci indique à pycharm qu'il s'attend à ce que la fonction soit appellée avec une str et un float et devrait
# retourner un float
print(afficher_nombre("Pier Luc", 42.0))

# Si je ne spécifie pas les bons types, PyCharm va me donner un avertissement. Cependant, ce sont juste des indices,
# donc pas d'erreur
print(afficher_nombre(42, 32))

# On peut faire ceci pour toute déclaration de variables
mon_int: int = 2
mon_float: float = 42.0
phrase: str = "Une str"
# etc...

# Si vous changez le type par mégarde, un avertissement apparaîtra
mon_float = "Pier Luc"

# Les builtins de python incluent tous les indices de type
math.sqrt(5.0)




