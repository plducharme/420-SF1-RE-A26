mot_de_passe = input('Entrez votre mot de passe: ')

raison = []
if len(mot_de_passe) < 8:
    raison.append('Trop  court')
if mot_de_passe.lower == mot_de_passe:
    raison.append('Aucune majuscule')