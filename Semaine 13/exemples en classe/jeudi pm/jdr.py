import random
import time


class Heros:

    def __init__(self, nom: str):
        self.nom = nom
        self.attaque = random.randint(4, 7)
        self.defense = random.randint(3, 4)
        self.pdv = random.randint(25, 35)
        self.bourse = 0


class Gobelin:

    def __init__(self):
        self.nom = random.choice(["Goby", "Marc", "Grognard", "Jean-François"])
        self.attaque = random.randint(2, 3)
        self.defense = random.randint(1, 3)
        self.pdv = random.randint(8, 12)
        self.type = "gobelin"


class Dragon:
    def __init__(self):
        self.nom = random.choice(["Smaug", "Krokmou", "Drogon", "Toothless"])
        self.attaque = random.randint(4, 6)
        self.defense = random.randint(5, 8)
        self.pdv = random.randint(15, 20)
        self.type = "dragon"


class Jeu:

    def __init__(self, nom_heros: str):
        self.heros: Heros = Heros(nom_heros)

    def combat(self):
        liste_monstres = [Gobelin(), Dragon()]
        monstre = random.choices(liste_monstres, k=1, weights=[80, 20])[0]

        while self.heros.pdv > 0 and monstre.pdv > 0:

            crit_heros = random.randint(1, 2)
            attaque_heros = max(crit_heros * self.heros.attaque - monstre.defense, 0)
            print(f"{self.heros.nom} attaque {monstre.nom} le {monstre.type} pour {attaque_heros}")
            monstre.pdv -= attaque_heros
            # attaque du monstre
            crit_monstre = random.randint(1, 2)
            attaque_monstre = max(crit_monstre * monstre.attaque - self.heros.defense, 0)
            print(f"{monstre.nom} le {monstre.type} attaque {self.heros.nom} pour {attaque_monstre}")
            self.heros.pdv += attaque_monstre

            time.sleep(1)

    def jouer(self):

        while True:
            self.combat()
            if self.heros.pdv < 0:
                print(f"Le héros est tombé au combat après une lutte acharnée!")
                break
            loot = random.choice(["potion", "or"])

            if loot == "potion":
                print(f"Une potion est tombé du monstre")
                self.heros.pdv += random.randint(5, 10)
            elif loot == "or":
                qte_or = random.randint(1, 3)
                print(f"Le monstre a laissé tombé {qte_or} pièces d'or.")
                self.heros.bourse += qte_or

            if self.heros.bourse > 15:
                print(f"Le héros a assez d'or pour prendre sa retraite!")
                exit()


nom = input("Entrez le nom du héros: ")

jeu = Jeu(nom)
jeu.jouer()
