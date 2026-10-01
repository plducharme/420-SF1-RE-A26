def bonjour():
    print("Salut de b")


MA_CONSTANTE = 5464738.89

print("print() dans la portée globale de module_b")
print(f"Le nom du module est <{__name__}>")

if __name__ == "__main__":
    print("Exécution du module b")
