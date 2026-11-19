scores = {
    "Nova": 1250,
    "Orion": 980,
    "Vega": 2100,
    "Luna": 1850
}

top_pilote: None | str = None

for pilote in scores.keys():
    if top_pilote is None:
        top_pilote = pilote
        continue
    if scores[top_pilote] < scores[pilote]:
        top_pilote = pilote
print(f"Meilleur pilote: {top_pilote} {scores[top_pilote]}")
meilleur = max(scores)
print(f"Meilleur pilote: {meilleur} {scores[meilleur]}")

