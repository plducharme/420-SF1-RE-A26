langue = ()
data = ((1, "Français", 20), (2, "Français", "Anglais", 30), (3, "Espagnole", "Arabe", 40))

# parcourir les codes de personnes
for t in data:
    print(t[0])

# On parcourt les tuples, data est un tuple contenant des tuples
for t in data:
    # On parcourt la partie du sous-tuple dans data, le sous-tuple est le tuple où l'on enlève le premier et dernier
    # élément
    # Ce "slicing" t[1:len(t)-1] retourne les éléments dans le milieu (sans le premier et le dernier)
    for j in t[1:len(t)-1]:
        if j in langue:  # "in" permet dew vérifier si un élément fait partie de la séquence (ici, un tuple)
            continue
        else:
            # Ici, on ne modifie pas le tuple, on le réassigne. On concatène la langue en réassignant le résultat
            langue = langue + (j, )

print(f"tuple langues: {langue}")

# Extraction de l'âge
age = ()
for i in data:
    age = age + (i[len(i)-1], )

print(f"âges: {age}")

# On peut utiliser les opérations disponibles sur les séquences
print(f"max(age): {max(age)}")
print(f"min(age): {min(age)}")
print(f"len(age): {len(age)}")
print(f"sum(age): {sum(age)}")

