
a = int(input("Entrez un nombre:\t"))

# si la condition est vrai, tout ce qui est indenté après les ":" sera exécuté
# si la condition est fausse, la condition du elif sera évaluée.
# on peut mettre plusieurs elif de suite
if a > 0:
    print(f"{a} est positif")
elif a < 0:
    print(f"{a} est négatif")

# Pas de else dans ce cas-ci
print("fin de programme")
