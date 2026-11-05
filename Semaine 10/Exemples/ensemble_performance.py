from time import perf_counter_ns

# Les ensembles sont très performants pour les tests d'appartenance ou pour les opérations des ensembles

# exemple si je veux savoir ce qui est commun entre deux listes
# liste contenant de paires
liste = [x for x in range(2, 501, 2)]
# liste des carrés
liste_carres = [c**2 for c in range(1, 501)]

# Vérifier les éléments communs de liste et liste_carres en utilisant une liste
temps_debut = perf_counter_ns()
liste_communs = []
for i in liste:
    for j in liste_carres:
        if i == j:
            liste_communs.append(i)
temps_fin = perf_counter_ns()
print(f"Temps pour comparer avec listes: {temps_fin - temps_debut} ns")

temps_debut = perf_counter_ns()
ensemble_liste = set(liste)
ensemble_carres = set(liste_carres)

ensemble_communs = ensemble_liste.intersection(ensemble_carres)
temps_fin = perf_counter_ns()
print(f"Temps pour comparer, ensembles (set): {temps_fin - temps_debut} ns")




