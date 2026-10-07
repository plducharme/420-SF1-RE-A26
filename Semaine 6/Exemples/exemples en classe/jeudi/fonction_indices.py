
# On peut ajouter les indices pour les types des paramètres
def salutations_nombre(nom: str, nombre: float) -> float:
    print(f"Bonjour {nom}, ton nombre préféré est {nombre}")
    return nombre**2


salutations_nombre("Pier Luc", 42.0)

salutations_nombre(666, 32)

# On peut ajouter un indice de type pour les variables déclarées

mon_int: int = 4
mon_float: float = 42.0
valeur_bool: bool = True

# Si vous changez le type, PyCharm donnera un avertissement
mon_float = "sdfsdfdsf"

