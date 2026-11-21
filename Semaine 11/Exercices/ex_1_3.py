# Demande la phrase à l'utilisateur
phrase = input('Phrase : ')

# Banque de voyelles
voyelles = 'aeiouyàâéèêëîïôöùû'

# Compte les voyelles et crée une nouvelle phrase en les remplaçant par *
nb_voyelles = 0
phrase_cryptee = ''
for lettre in phrase:
    if lettre.lower() in voyelles:
        nb_voyelles += 1
        phrase_cryptee += '*'
    else:
        phrase_cryptee += lettre

# Affiche les phrases demandées
print(phrase.upper())
print('Voyelles :', nb_voyelles)
print(phrase_cryptee)
