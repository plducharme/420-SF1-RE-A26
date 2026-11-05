import requests

numero_poke = int(input("Entrez un numéro de pokémon: "))

dict_pokemon: dict = requests.get(f"https://pokeapi.co/api/v2/pokemon/{numero_poke}").json()


id_pokemon = dict_pokemon["id"]
print("ID du Pokémon:", id_pokemon)
print("Nom:", dict_pokemon["name"])

abilitees_pokemon = dict_pokemon["abilities"]

for abiliter_pokemon in abilitees_pokemon:
    abilite_pokemon = abiliter_pokemon["ability"]
    print("Abilitées du Pokémon:", abilite_pokemon["name"])

for cle, valeur in dict_pokemon.items():
    print(f"Clé: {cle}, Valeur: {valeur}")
