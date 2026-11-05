# On a vu remove() et pop(), mais il existe d'autres fonctions sur les listes
# https://docs.python.org/fr/3.14/builtins/stdtypes.html#lists
# https://docs.python.org/fr/3.14/builtins/stdtypes.html#typesseq-common
# https://docs.python.org/fr/3.14/builtins/stdtypes.html#typesseq-mutable
lettres = ["a", "b", "c", "b"]

# index() retourne l'index de la première occurrence de l'élément passé en paramètre; déclanche une erreur
# si non-existant
print(lettres.index("b"))

# count() retourne le nombre d'occurrences de l'élément dans la liste, déclanche une erreur si non existant
print(lettres.count("b"))

# "in" teste l'appartenance à une séquence
if "z" in lettres:
    print(lettres.index("z"))
else:
    print("z n'est pas dans la liste")

if "b" in lettres:
    print(lettres.count("b"))

if "j" not in lettres:
    print("j n'est pas dans la liste")

# Petit rappel: <element in liste> retourne True ou False
# On peut donc se faciliter la vie parfois

# Solution 1
lettre_trouvee = False
if "b" in lettres:
    lettre_trouvee = True
print(lettre_trouvee)
# Solution plus courte
lettre_trouvee = "b" in lettres
print(lettre_trouvee)
