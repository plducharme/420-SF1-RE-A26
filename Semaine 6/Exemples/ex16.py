from math import pow, log
from random import seed, random
# Ceci importe seulement ce que l'on a de besoin. Pas besoin de préfixer

seed(42)
nombre = random()
log_nombre = log(nombre)
puissance = pow(log_nombre, 3.0)

print(globals())


