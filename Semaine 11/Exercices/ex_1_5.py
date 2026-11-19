import random
prenom = input("Prénom : ")
nom = input("Nom : ")
titre = ["le Redoutable", "le Badass", "le SuperHot"]
# découpage/slicing [debut : fin non incluse : pas]
print(f"Ton nom de dragon : {prenom[:3]}{nom[-3::1]} {random.choice(titre)}")
