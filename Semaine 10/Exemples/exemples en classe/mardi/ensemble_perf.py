from time import perf_counter_ns

liste_impair = [x for x in range(1, 100000, 2)]
# Équivalent à
# for i in range(1, 100000, 2):
#     liste_impair.append(i)
liste_fonction = [x**2-1 for x in range(1, 50000)]

# temps_debut = perf_counter_ns()
# liste_communs = []
# for i in liste_impair:
#     for j in liste_fonction:
#         if i == j:
#             liste_communs.append(i)
# temps_fin = perf_counter_ns()
# print(f"Temps pour parcourir les listes: {temps_fin-temps_debut} ns")

temps_debut = perf_counter_ns()
ensemble_impair = set(liste_impair)
ensemble_fonction = set(liste_fonction)
commun = ensemble_impair.intersection(ensemble_fonction)
liste_communs = list(commun)
temps_fin = perf_counter_ns()
print(f"Temps pour comparer les ensembles: {temps_fin-temps_debut} ns")