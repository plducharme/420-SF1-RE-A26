mineraux = []

symboles = {
    "Fer": "Fe",
    "Or": "Au",
    "Argent": "Ag",
    "Plomb": "Pb"
}


while True:

    ajout_minerai = input("Ajoutez un minerai: ")
    mineraux.append(ajout_minerai)

    if len(mineraux) == 5:
        break

print("Minéraux récoltés : ")
for m in mineraux:
    # Afficher le symbole si connu dans le dictionnaire
    # if m in symboles:
    #     print(f"- {symboles.get(m)}")
    # else:
    #     print(f"- {m}")
    print(f"- {symboles.get(m, m)}")



