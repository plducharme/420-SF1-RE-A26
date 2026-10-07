from module_a import *
from module_b import *
# bonjour existe dans les 2 modules, la dernière version importée sera utilisée
bonjour()

# dans les modules importés, faire un print(__name__) retourne le nom du module
# Faire la même chose dans le script principal (celui exécuté) va retourner "__main__"
print(__name__)

# On peut utiliser ceci, pour s'assurer que du code soit seulement exécuté s'il est dans le script principal
if __name__ == "__main__":
    print("Module conflit.py")
