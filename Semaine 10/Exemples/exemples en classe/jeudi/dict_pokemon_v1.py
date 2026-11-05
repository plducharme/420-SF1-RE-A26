import requests

while True:
    numero_poke = int(input("\nEntrez un numéro de pokémon: "))
    dict_pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{numero_poke}").json()
    print(f"name of pokemon : {dict_pokemon["name"]}")
    print("abilities : ", end="")
    for element in dict_pokemon["abilities"]:
        print(element["ability"]['name'], end='\t')
