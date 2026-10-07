from math import *
# En utilisant *, tout est importé, mêm ce qui ne sera pas utilisé. Faire attention aux conflits!
# En utlisant cette notation, on a pas besoin de préfixer l'appel avec le nom du module

nombre = 121
# pi est défini dans math
angle = pi / 6
# sqrt() et sin() sont aussi définis dans math
print("Racine carré de 121:", sqrt(nombre))
print("Sinus de 30 degrés:", sin(angle))

# Les définitions de fonctions se retrouvent maintenant dans les globales
print(globals())
