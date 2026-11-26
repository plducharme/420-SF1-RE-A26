# Passage d’un nombre arbitraire d’arguments
def f(*args):
    print(*args)


f(3, 5)  # affiche 3, 5
f(3)  # affiche 3
f(3, "Bonjour", 5, True, -0.25)  # affiche 3,Bonjour,5,true,-0.25


# Le *args est le tuple contenant tous les arguments passés
def somme(*args):
    total = 0
    for i in args:
        total += i
    return total


print(somme(1))
print(somme(1, 2, 3, 4, 5))


# pour les arguments nommés, on peut utiliser **kwargs pour obtenir un dict à partir d'un nombre illimité d'arguments
def stats(**kwarg):

    for cle, valeur in kwarg.items():
        print(f"{cle} : {valeur}")


stats(force=15, agilite=6, hp=78)


# Tout ceci est du "unpacking"
def calcul_somme_produit(a: float, b: float):
    return a + b, a * b


retour = calcul_somme_produit(3.2, 4.2)
# Quand on retourne 2 valeurs dans une fonction, le retour est un tuple contenant les valeurs
print(retour)
# Ceci déballe (unpack) le tuple dans deux variables
somme1, produit = calcul_somme_produit(7, 3)
print(somme1, produit)
# Même chose:
somme2, produit2 = retour
print(somme2, produit2)


