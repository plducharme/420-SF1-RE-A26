phrase = input("Phrase : ")
phrase = phrase.replace(" ", "")

frequences = {}

for lettre in phrase:
    frequences[lettre] = frequences.get(lettre, 0) + 1
print(frequences)

plus_frequente = ""

for lettre, freq in frequences.items():
    if frequences.get(plus_frequente, 0) < frequences[lettre]:
        plus_frequente = lettre
print(f"Lettre la plus fréquente : {plus_frequente} ({frequences[plus_frequente]} fois)")
