# On peut suggérer à Python les types attendus
# PyCharm vous donnera des "warnings" si vous ne respectez pas le type

mon_int: int = 5

# Avertissement qu'il s'attend à un int, mais le code va exécuter
mon_int = "une str"

print(mon_int)


class Jeu:
    def __init__(self, nom: str, annee_sortie:int):
        self.nom: str = nom
        self.annee: int = annee_sortie

    # On peut spécifier le type de retour
    def nom_annee(self) -> str:
        return f"{self.nom} {self.annee}"


gta6 = Jeu("GTA VI", 2026)
gyk2 = Jeu("Graveyard Keeper 2", 2026)
tape_2_tape = Jeu("Tape 2 Tape", 2026)

print(gta6.nom_annee())
# nom_annee() retourne une str, mon_int s'attend à avoir un int
mon_int = gyk2.nom_annee()

# on peut spécifier les types attendus dans des structures de données
liste_jeux: list[Jeu] = [gta6, gyk2, tape_2_tape]
