# Classe Personne
class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.adresse = "LAVAL"

    # Méthodes
    def veillir(self):
        self.age += 1

    def info(self):
        print("Prenom=" + self.prenom + " Nom=" + self.nom + " Age=" + str(self.age) + " Adresse=" + self.adresse)

    def to_string(self):
        return "Prenom: " + self.prenom + " Nom: " + self.nom + " Age: " + str(self.age) + " Adresse: " + self.adresse

    # Implémenter __repr__ permet de changer la représentation de l'objet lorsque l'on fait un print()
    # Au lieu d'afficher le type et son adresse mémoire, cela va afficher la str retournée
    def __repr__(self):
        return "Prenom: " + self.prenom + " Nom: " + self.nom + " Age: " + str(self.age) + " Adresse: " + self.adresse


# Ex d’utilisation : on crée deux objets de type personnes
les_personnes = list()
# afficher les personnes dans une boucle
nb = int(input("nombre de personnes dans la liste: "))
for i in range(nb):
    prenom = input(" personne " + str(i) + " \nvotre prenom: ")
    nom = input("votre nom: ")
    age = input("votre age: ")
    les_personnes.append(Personne(prenom, nom, age))
    print(les_personnes[i].to_string())

    # Si __repr__ est implémenté, on peut faire ceci directement :
    print(les_personnes[i])
