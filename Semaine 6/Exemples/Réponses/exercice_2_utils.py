
def renverse_chaine(chaine: str):
    chaine_inversee = ""
    for s in chaine:
        chaine_inversee = s + chaine_inversee
    return chaine_inversee


def renverse_chaine_v2(chaine: str):
    return chaine[::-1]


if __name__ == "__main__":
    # Tests pour s'assurer que cela fonctionne
    assert renverse_chaine("Allo les amis!") == "!sima sel ollA"
    print(renverse_chaine_v2("Allo les amis!"))
