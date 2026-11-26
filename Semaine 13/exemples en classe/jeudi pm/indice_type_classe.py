
class Film:

    def __init__(self, titre: str, annee: int, realisateur: Realisateur):
        self.titre = titre
        self.annee = annee
        self.realisateur = realisateur

    def __repr__(self):
        return f"{self.titre}|{self.annee}|{self.realisateur}"


class Realisateur:
    def __init__(self, nom: str, prenom: str):
        self.prenom = prenom
        self.nom = nom

    def __repr__(self):
        return f"Réalisateur:{self.nom}, {self.prenom}"


hitchcock = Realisateur("Hitchcok", "Alfred")
lang = Realisateur("Lang", "Fritz")

psycho = Film("psychose", 1960, hitchcock)
m_le_maudit = Film("M", 1931, lang)

biblio_films = [psycho, m_le_maudit]

print(biblio_films)
print(Film("Dune pt3", 2026, Realisateur("Villeneuve", "Denis")))

