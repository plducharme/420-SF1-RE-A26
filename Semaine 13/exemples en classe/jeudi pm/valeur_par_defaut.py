class Moteur:

    def __init__(self, hp: int, grosseur: float, type_moteur: str = "thermique"):
        self.hp = hp
        self.grosseur = grosseur
        # type_moteur est celui passé en paramètre, mais le paramètre a une valeur par défaut si non spécifié
        self.type = type_moteur
        # valeur par défaut non passé en paramètre
        self.fabricant = "Dodge"


moteur_challenger_srt8 = Moteur(470, 6.2)
moteur_kia_soul_ev = Moteur(201, 1.4, type_moteur="électrique")
moteur_kia_soul_ev.fabricant = "Kia"
