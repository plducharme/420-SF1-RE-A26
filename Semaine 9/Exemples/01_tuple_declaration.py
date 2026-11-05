# On peut omettre les parenthèses lors de la déclaration
tuple1 = "a", "b", "c", "d"

tuple2 = ("a", "b", "c", "d")

# Un tuple peut contenir n'importe quel type
tuple3 = (1, 42, 666, 65)
tuple4 = (2.0, 4.8, 9.5)

# On peut mélanger les types comme dans les listes, mais ce n'est pas recommandé
tuple5 = (1, "Chimie Organique", 2.0, False, [1, 2, 3, 4])

# Comme on peut avoir n'importe quel type, on peut avoir, entre autres, un tuple contenant des tuples
tuple6 = ((1, "Français"), (2, "Français", "Anglais"))

# Si on veut déclarer un tuple contenant seulement un élément, il faut mettre une virgule après le premier élément
tuple7 = (1, )
print(type(tuple7))
# Sinon, python va considérer les parenthèses comme faisant partie d'une expression mathématique
non_tuple = (1)
print(type(non_tuple))

# On peut utiliser aussi le constructeur tuple(séquence)
tuple_liste = tuple([42, 65, 23, 56])
print(f"tuple_liste: {tuple_liste}")

# Faire attention, comme pour le constructeur de liste (i.e. liste()), le constructeur de tuple (i,e, tuple())
# va initialiser un tuple avec chaque caractère de la str
tuple_str = tuple("patate")
print(tuple_str)


