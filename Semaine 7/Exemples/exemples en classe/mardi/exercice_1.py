t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre',
      'Décembre']


# solution 1
for i in range(len(t1)):
    t2.insert(2 * i + 1, t1[i])

print(t2)

t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre',
      'Décembre']

# solution 2
t3 = []

for i in range(len(t1)):
    t3 += [t2[i]] + [t1[i]]

t2 = t3
print(t2)


t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre',
      'Décembre']
# Solution 3
delta = 0
for idx, jours in enumerate(t1):
    # on doit insérer après le mois, donc on doit insérer 1 plus loin (plus le delta) que l'itération en cours
    t2.insert(idx+1+delta, jours)
    delta += 1
print(t2)


