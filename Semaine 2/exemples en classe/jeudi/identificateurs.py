# Un identificateur ne peut pas commencer par un chiffre
# 1temperature = 54


# Ces identificateurs sont valides, mais ne respecte pas les PEP-008
Mon_super_Identificateur = 42
PatateEnPoudre = 42

# pass est une instruction qui ne fait rien, mais permet au programme d'être syntaxiquement valide
for i in range(6):
    pass
j = 6

# Soft keywords peuvent être des identificateurs tout dépendant du contexte
match = 3
case = 4

nombre = int(input("Entrez un nombre: "))

match nombre:
    case 1:
        print("C'est 1")
    case 42:
        print("La réponse à tout")
    case _:
        print("Autre chose")

