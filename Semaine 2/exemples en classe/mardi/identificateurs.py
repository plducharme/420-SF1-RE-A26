# Valide syntaxiquement
patate = 0
patate2 = 0
M0nna = 0
_patate = 0
ma_super_patate = 0
Patate = 0
# Pas valide:
#1Patate = 0
#@patate = 0
#élève = 0

# match case peuvent être des identificateurs, mais peuvent être réservés
match = 9
case = 4

x = int(input("Entrer un nombre: "))

match x:
    case 2:
        print("C'est un 2")
    case 42:
        print("La réponse à tout")
    case _:
        print("C'est autre chose")

# variables doivent être en snake case
coord_x = 4
coord_y = 3
age_personnage = 18






