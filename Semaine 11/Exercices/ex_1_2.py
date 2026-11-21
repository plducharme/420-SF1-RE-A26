# Demande à l'utilisateur de saisir le mot de passe
mot_de_passe = input('Entrez votre mot de passe: ')

# Crée un ensemble vide et y ajoute les raisons du refus
raisons = set()
if len(mot_de_passe) < 8:
    raisons.add('Trop court')
if mot_de_passe.lower() == mot_de_passe:
    raisons.add('Aucune majuscule')
if not any(lettre.isdigit() for lettre in mot_de_passe):
    raisons.add('Aucun chiffre')

# Ouvre la porte si le mot de passe est valide, explique pourquoi sinon
if not raisons:
    print('Porte ouverte')
else:
    print('Porte verrouillée\nRaison(s):', ', '.join(raisons))
