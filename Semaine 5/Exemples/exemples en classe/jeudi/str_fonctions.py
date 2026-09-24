# on peut appeler des fonctions sur des str

citation = "Il y a 10 sortes de gens sur Terre : ceux qui connaissent le binaire, et les autres."
# str.count(sous-chaîne, debut) compte le nombre d'occurences d'une sous-chaîne dans la str, debut (optionnel)
# commence à cet index au lieu du début de la str
print(citation.count("re"))

# find(sous-chaîne) permet de trouver l'index de la sous-chaîne dans la str, retourne -1 si inexistante
print(citation.find("re"))
print(citation.find("aaaaa"))
# rfind(sous-chaîne) commence la recherche par la droite (par la fin)
print(citation.rfind("re"))

# endswith(sous-chaîne) retourne True si la str se termine par la sous-chaîne
# il y a des paramètres optionnels pour indiquer l'intervalle considéré
print(citation.endswith("."))


