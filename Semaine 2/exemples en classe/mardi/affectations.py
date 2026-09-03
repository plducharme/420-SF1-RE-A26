base = 3
hauteur = 4
hypothenuse = (base**2 + hauteur**2)**0.5
print(hypothenuse)
# En assignant une variable, il réserve un emplacement qui contient la valeur assignée, si on réassigne, ça change la
# valeur de cet emplacement
base = 6
# Si j'assigne une variable à None, elle a une place en mémoire, mais pas de valeur
b = None

n = 9
x = 1
n = x + 12

i = 9
j = 1
i = j
j = i

# Affectations multiples
c = d = 63  # dans ce cas-ci c et d égalent 63
print(c, d)
# Autre façon de faire une affectation multiple
o, p = 3, 7
print(o, p)

# Affectations parallèles
k, z = 67, 8.3
print(k, z)

# Si on veut inverser deux variables, ex: a devient b et b devient a
a = 5
b = 42
print(a, b)
tmp = a
a = b
b = tmp
print(a, b)

# Autre façon d'inverser
var1 = 42
var2 = 666
print(var1, var2)
# on peut utiliser l'affectation multiple pour inverser
var1, var2 = var2, var1
print(var1, var2)



