
class Telephone:

    def __init__(self, marque: str, modele: str, quantite: int):
        self.marque = marque
        self.modele = modele
        self.quantite = quantite

    def __add__(self, other):
        return self.quantite + other.quantite

    def __eq__(self, other):
        if self.modele != other.modele:
            return False
        elif self.marque != other.marque:
            return False
        elif self.quantite != other.quantite:
            return False
        else:
            return True


pixel_10 = Telephone("Google", "Pixel 10", 8)
duo = Telephone("Apple", "Duo", 7)

mes_telephones = pixel_10 + duo
# Python fait en dessous du capot
qte_tel = pixel_10.__add__(duo)
print(mes_telephones)
print(qte_tel)

if pixel_10 == duo:
    print("Égal")
else:
    print("Pas égal")
