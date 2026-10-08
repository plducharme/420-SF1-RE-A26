
a = int(input("Entrez un nombre:\t"))

# si la condition est vrai, tout ce qui est indenté après les ":" sera exécuté
# si la condition est fausse, la condition du elif sera évaluée.
# on peut mettre plusieurs elif de suite
# si aucun des if et elif n'est vrai, le bloc else est alors exécuté
if a > 0:
    print("a est positif")
elif a < 0:
    print("a est négatif")
else:
    print("a est égal à zéro")

print("Fin du programme!")