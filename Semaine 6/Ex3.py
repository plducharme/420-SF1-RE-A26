liste_acides = 'ARWG'
sequence_acides = input("Entrez la séquence d'acides aminés: ")

while sequence_acides not in liste_acides:
    print('Veuillez entrer une séquence valide')
    input('')
