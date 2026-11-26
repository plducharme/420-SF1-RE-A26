import requests


class Pokemon:

    def __init__(self, config_pokemon: dict):
        self.id = config_pokemon["id"]
        self.nom = config_pokemon["name"]
        self.moves: list[Move] = []

        liste_moves = config_pokemon["moves"]

        for move in liste_moves:
            self.moves.append(Move(move["move"]["name"], move["move"]["url"]))

    def __repr__(self):
        return f"Pokemon: {self.nom} moves: {self.moves}"


class Move:
    def __init__(self, nom: str, url: str):
        self.nom = nom
        self.url = url

    def __repr__(self):
        return f"{self.nom}"


class Pokedex:
    def __init__(self):
        self.liste_pokemon: list[Pokemon] = []

    def __repr__(self):
        return f"Mes pokemon: {self.liste_pokemon}"


url_de_base = "https://pokeapi.co/api/v2/pokemon/"
pokedex = Pokedex()
while True:
    numero_pokemon = input("Entrez un numéro de pokemon (-1) pour quitter: ")

    if numero_pokemon == "-1":
        print(pokedex)
        break
    pokemon_dict = requests.get(f"{url_de_base}{numero_pokemon}").json()
    pokemon = Pokemon(pokemon_dict)
    pokedex.liste_pokemon.append(pokemon)





