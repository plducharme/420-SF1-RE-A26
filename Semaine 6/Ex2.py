def est_composable():
    if mot in sequence or mot in sequence_inverse:
        return f"Le mot {mot} est composable à partir de {sequence}"
    else:
        return f"Le mot {mot} n'est pas composable à partir de {sequence}"


mot = input('Entrez le mot: ')
sequence = input('Entrez la séquence: ')
sequence_inverse = sequence[::-1]

print(est_composable())
