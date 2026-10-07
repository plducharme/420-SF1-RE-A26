import math, random
# Bien que syntaxiquement légale, un import de plusieurs sur une même ligne, est une violation des PEP-008
# Il faudrait faire deux imports sur des lignes séparées
# import math
# import random

# Dans tous les cas, on préfixe avec le nom du module
# random.seed() avec une valeur, permet de générer les mêmes nombres aléatoires à chaque exécution
random.seed(42)
nombre = random.random()

print("Nombre:", nombre)
log_nombre = math.log(nombre)
puissance = math.pow(log_nombre, 3.0)

print("le log du nombre", log_nombre)
print("le cube de", log_nombre, "est", puissance)


