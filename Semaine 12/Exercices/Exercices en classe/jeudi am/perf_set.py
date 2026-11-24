from time import perf_counter_ns

liste_paires = [x for x in range(0, 25000, 2)]
liste_carres = [x**2 for x in range(0, 25000)]

temps_debut = perf_counter_ns()
liste_communs = []
for i in liste_paires:
    for j in liste_carres:
        if i == j:
            liste_communs.append(i)
temps_fin = perf_counter_ns()
print(f"Temps listes imbriquées: {temps_fin - temps_debut} ns")

temps_debut = perf_counter_ns()
ensemble_paires = set(liste_paires)
ensemble_carres = set(liste_carres)

ensemble_commun = ensemble_paires & ensemble_carres
liste_communs = list(ensemble_commun)
temps_fin = perf_counter_ns()
print(f"Temps ensembles: {temps_fin - temps_debut} ns")


