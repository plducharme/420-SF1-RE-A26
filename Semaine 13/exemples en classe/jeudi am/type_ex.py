class Personne:
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age

    def __repr__(self):
        return f"[nom={self.nom}, age={self.age}]"


lucien = Personne("Lucien", 4)
print(lucien)

print(type(lucien))
age = 18

mon_int = int("5")


print(type(age))
print(type(mon_int))
print(mon_int)


