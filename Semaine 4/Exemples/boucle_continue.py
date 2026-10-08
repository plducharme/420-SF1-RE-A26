# continue permet d'exécuter la prochaine itération en sautant les instructions restantes de la boucle

for nbr in range(2, 10):
    if nbr % 2 == 0:
        print(f"{nbr} est pair")
        continue
    print(f"{nbr} est impair")
