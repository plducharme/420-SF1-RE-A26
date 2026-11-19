import requests

numero_pokemon = input("Entrez un numéro de pokemon: ")
url_de_base = "https://pokeapi.co/api/v2/pokemon/"
pokemon_dict = requests.get(f"{url_de_base}{numero_pokemon}").json()

print(f"Pokemon choisi: {pokemon_dict["name"]}")

liste_abilities = pokemon_dict["abilities"]

for ability_dict in liste_abilities:
    print(f"\tHabileté: {ability_dict["ability"]["name"]}")




