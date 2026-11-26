mot_de_passe = input("Mot de passe : ")

raisons = []
# vérifie la longueur
if len(mot_de_passe) < 8:
    raisons.append("trop court")
# Si le mot de passe mis en minuscule égale le mot de passe orginal, le mot de passe était déjà en minuscules
if mot_de_passe.lower() == mot_de_passe:
    raisons.append("aucune majuscule")
# regarde s'il y a au moins un chiffre
a_un_chiffre = False
for c in mot_de_passe:
    # "in" permet de faire un test d'appartenance à une séquence (liste, str, tuple) ou à un map (clé d'un dict)
    if c in "1234567890":
        a_un_chiffre = True
        break
if not a_un_chiffre:
    raisons.append("aucun chiffre")
# Si la liste est vide, le mot de passe rempli toutes les conditions
if len(raisons) == 0:
    print("Porte ouverte")
else:
    print(f"Porte verrouillée : ", end="")
    for r in raisons:
        print(r, end=", ")
