import random
import math
import time


liste_loot = ["potion", "or", "amulette", "épée", "armure"]


def creer_gobelin() -> dict:
    gobelin = {
        "pdv": random.randint(2, 8),
        "att": random.randint(1, 2),
        "def": random.randint(0, 1),
        "nom": "gobelin"
    }
    return gobelin


def creer_heros() -> dict:
    heros = {
        "pdv": random.randint(15, 30),
        "att": random.randint(5, 7),
        "def": random.randint(1, 5),
        "inventaire": set(),
        "bourse": 0
    }
    return heros


def creer_dragon() -> dict:
    dragon = {
        "pdv": random.randint(25, 35),
        "att": random.randint(3, 6),
        "def": random.randint(3, 4),
        "nom": "dragon"
    }
    return dragon


def combat(heros: dict, monstre: dict):
    pdv_heros = heros["pdv"]
    pdv_monstre = monstre["pdv"]

    print(f"Combat en le héros et un {monstre["nom"]}")
    while pdv_heros > 0 and pdv_monstre > 0:

        attaque_heros = heros["att"] * random.randint(1, 2)
        defense_monstre = monstre["def"]
        pdv_monstre -= attaque_heros - defense_monstre
        pdv_monstre = max(pdv_monstre, 0)
        print(f"Le héros attaque le monstre pour {attaque_heros}")
        print(f"Il reste {pdv_monstre} pdv au {monstre["nom"]}")

        attaque_monstre = monstre["att"] * math.floor(random.uniform(1.0, 2.0))
        def_heros = heros["def"]
        pdv_heros -= attaque_monstre - def_heros
        pdv_heros = max(pdv_heros, 0)

    if pdv_heros < 0:
        print(f"Le héros est décédé de façon glorieuse!")
        exit()

    print(f"Le héros a vaincu le {monstre["nom"]}")
    # mettre à jour les pdv du héros
    heros["pdv"] = pdv_heros
    item_loot = random.choice(liste_loot)
    print(f"Le héros a trouvé {item_loot}")

    if item_loot == "potion":
        guerison = random.randint(10, 15)
        print(f"La potion a guéri pour {guerison} pdv")
        heros["pdv"] = heros["pdv"] + guerison
    elif item_loot == "or":
        or_gagne = random.randint(1,2)
        heros["bourse"] += or_gagne
        print(f"Le butin comprenait {or_gagne} pièces d'or")
    else:
        heros["inventaire"].add(item_loot)


heros = creer_heros()
while True:

    print(f"Le héros continue sa quête")

    monstre = random.choices(["gobelin", "dragon"], weights=[90, 10], k=1)[0]

    if monstre == "gobelin":
        gobelin = creer_gobelin()
        combat(heros, gobelin)
    else:
        dragon = creer_dragon()
        combat(heros, dragon)

    if heros["bourse"] >= 10:
        print(f"Le héros se retire au chaud avec {heros["bourse"]} pièces d'or")
        break

    time.sleep(0.5)





