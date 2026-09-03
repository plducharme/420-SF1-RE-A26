# affectation pour pythagore
a = 3
b = 4
c = (a**2 + b**2)**0.5

print("hypothénuse: ", c)

# Si vous réaffectez une variable sans l'utiliser d'abord, il y aura un avertissement
x = 5
x = 6

# Si on veut interchanger les valeurs de 2 variables
var1 = 42
var2 = 666
print("Avant: ", var1, var2)
tmp = var1
var1 = var2
var2 = tmp

print("Après:", var1, var2)

# Autre solution en utilisant l'affectation parallèle
var3 = 56
var4 = 67
print("Avant var3 var4: ", var3, var4)
var3, var4 = var4, var3
print("Après var3 var4: ", var3, var4)

# Explication optionnelle
# lors de l'affectation, python mets les termes dans des tuples
# ce qui équivaut:
(var3, var4) = (var4, var3)


# Affectations multiples
i = j = k = 1234
print(i, j, k)

# affectations parallèles
p1, p2 = 4, 432
print(p1, p2)





