
couleur_fruit = input("Quel est la couleur de votre fruit?\t")

# on peut imbriquer une structure conditionnelle à l'intérieur d'un autre structure conditionnelle
# il faut simplement s'assurer d'indenter nos blocs correctement
if couleur_fruit == "rouge":
    grosseur = input("Est que le fruit est petit [oui/non]: ")
    if grosseur == "oui":
        print("Votre fruit est p-e une fraise ou une framboise")
    elif grosseur == "non":
        print("C'est p-e une pomme ou un melon d'eau")
    else:
        print("réponse non gérée")
elif couleur_fruit == "bleu":
    print("votre fruit est p-e un bleuet")
elif couleur_fruit == "orange":
    peau = input("Est-ce que la peau du fruit est dur [oui/non]")
    if peau == "oui":
        print("C'est p-e une orange")
    else:
        print("C'est p-e une mandarine")
else:
    print("Ne connait pas cette couleur")

print("Fin du programme")
