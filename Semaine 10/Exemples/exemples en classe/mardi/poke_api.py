import requests

numero_poke = int(input("Entrez un numéro de pokémon: "))

dict_pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{numero_poke}").json()

# Liste des moves du pokemon


listes_moves_dict = dict_pokemon["moves"]
liste_moves_pokemon = []

# Liste des moves du pokemon
for move_dict in listes_moves_dict:
    liste_moves_pokemon.append(move_dict["move"]["name"])

print(f"Listes des moves du pokemon {dict_pokemon["name"]}: {liste_moves_pokemon}")

# Stats du pokemon
stats_pokemon = {}

for stat_dict in dict_pokemon["stats"]:
    cle = stat_dict["stat"]["name"]
    valeur = stat_dict["base_stat"]
    stats_pokemon[cle] = valeur

print(f"dictionnaire stats: {stats_pokemon}")

print("Statistiques")
for cle, val in stats_pokemon.items():
    print(f"\t{cle}: {val}")




