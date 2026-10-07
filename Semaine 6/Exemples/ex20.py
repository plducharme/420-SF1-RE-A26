def moyenne(somme_notes, nombre_etudiants):
    # Ce assert lèvera un AssertionError si le nombre d'étudiant est 0
    assert nombre_etudiants != 0
    # Si somme_notes n'est pas >= 0, un AssertionError sera levé avec le message après la virgule
    assert somme_notes >= 0, "La somme des notes doit être 0 ou positive"
    return somme_notes / nombre_etudiants


moyenne(250, 16)
# moyenne(250, 0)
moyenne(-1, 16)

