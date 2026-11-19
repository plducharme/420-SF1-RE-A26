energie = int(input("Énergie : "))

etat = ""
if 80 <= energie <= 100:
    etat = "Excellent"
elif 40 <= energie <= 79:
    etat = "Stable"
elif 1 <= energie <= 39:
    etat = "Critique"
else:
    etat = "Hors Service"

print(f"État du vaisseau: {etat}")

