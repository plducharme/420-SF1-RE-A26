phrase = input("Phrase : ")
# On enlève ales espaces
phrase = phrase.replace(" ", "")
# on construit le dictionnaire
frequences = {}
for lettre in phrase:
    frequences[lettre] = frequences.get(lettre, 0) + 1
print(frequences)

lettre_max = None
for lettre, freq in frequences.items():
    if lettre_max is None:
        lettre_max = lettre
    else:
        if frequences[lettre_max] < frequences[lettre]:
            lettre_max = lettre

# Autre façon en une ligne, key= spécifie la fonction à appeler pour comparer
# lettre_max = max(frequences, key=frequences.get)

print(f"Lettre la plus fréquente : {lettre_max} ({frequences[lettre_max]} fois)")





