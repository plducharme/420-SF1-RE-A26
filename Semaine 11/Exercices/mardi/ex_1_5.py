import random
prenom = input("Prénom : ")
nom = input("Nom: ")
titres = ["le redoutable", "le badass", "le puissant"]
print(f"Ton nom de dragon : {prenom[0:3]}{nom[-3:]} {random.choice(titres)}")

