potion = {'herbe', 'miel', 'cristal', 'eau'}

ingredients_str = input("Ingrédients : ")
ingredients_set = set(ingredients_str.split(","))

if potion.issubset(ingredients_set):
    print("Potion prête !")
else:
    manquants_set = potion - ingredients_set
    print(f"Il manque : {", ".join(manquants_set)}")
inutiles = ingredients_set - potion
print(f"Inutiles : {", ".join(inutiles)}")

