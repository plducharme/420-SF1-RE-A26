import requests

numero_poke = int(input("Entrez un numéro de pokémon: "))

dict_pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{numero_poke}").json()

print(dict_pokemon)




