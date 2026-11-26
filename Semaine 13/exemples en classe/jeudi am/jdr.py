import random
import time


class JeuDeRole:
    def __init__(self, nom_heros: str):
        self.heros: Heros = Heros(nom_heros)

    def jouer(self):
        while True:
            self.combat()
            if self.heros.pdv <= 0:
                print(f"Le héros est mort glorieusement!")
                break
            loot = random.choice(["potion", "or"])

            if loot == "potion":
                self.heros.pdv += random.randint(5, 10)
            elif loot == "or":
                self.heros.bourse += random.randint(1, 3)

            if self.heros.bourse >= 10:
                print(f"{self.heros.nom} est assez riche pour prendre sa retraite!")
                exit()

    def combat(self):
        liste_monstres = [Gobelin(), Dragon()]
        # random.choices() permet de sélectionner k éléments d'une liste en spécifiant des poids pour ces éléments
        monstre_combat = random.choices(liste_monstres, k=1, weights=[80, 20])[0]

        print(f"{self.heros.nom} rencontre {monstre_combat.nom} le {monstre_combat.type}!")

        while self.heros.pdv > 0 and monstre_combat.pdv > 0:
            crit_heros = random.randint(1, 2)
            # Le héros attaque en premier
            attaque_heros = max(self.heros.attaque * crit_heros - monstre_combat.defense, 0)
            print(f"{self.heros.nom} attaque le {monstre_combat.type} pour {attaque_heros}")
            monstre_combat.pdv -= attaque_heros
            # Le monstre attaque
            crit_monstre = random.randint(1, 2)
            attaque_monstre = max(monstre_combat.attaque * crit_monstre - self.heros.defense, 0)
            print(f"Le monstre attaque {self.heros.nom} pour {attaque_monstre}")
            self.heros.pdv -= attaque_monstre
            # Le programme va dormir pendant 1 seconde
            time.sleep(1)


class Heros:

    def __init__(self, nom: str):
        self.nom: str = nom
        self.pdv: int = random.randint(25, 50)
        self.attaque: int = random.randint(5, 7)
        self.defense: int = random.randint(3, 4)
        self.bourse: int = 0


class Gobelin:
    def __init__(self):
        self.nom: str = random.choice(["Bleurk", "Grognard", "Jean-Jacques"])
        self.pdv: int = random.randint(7, 10)
        self.attaque: int = random.randint(2, 3)
        self.defense: int = random.randint(1, 3)
        self.type: str = "gobelin"


class Dragon:
    def __init__(self):
        self.nom: str = random.choice(["Smaug", "Arathnos", "Aline"])
        self.pdv: int = random.randint(15, 20)
        self.attaque: int = random.randint(4, 5)
        self.defense: int = random.randint(4, 5)
        self.type: str = "dragon"


nom_heros = input("Entrez le nom du héros : ")
jeu = JeuDeRole(nom_heros)
jeu.jouer()

