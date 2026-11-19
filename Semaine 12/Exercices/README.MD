# 🚀 Mission Python : Agence Spatiale Intergalactique

Bienvenue dans l'Agence Spatiale Intergalactique ! Chaque mission vous permettra de pratiquer différentes notions de Python tout en explorant la galaxie.

---

# 🌍 Niveau 1 - Les chaînes de caractères (`str`)

## Exercice 1 : Carte d'identité cosmique

Demandez le nom d'un astronaute.

Affichez :

- son nom en majuscules ;
- son nom en minuscules ;
- le nombre de caractères ;
- la première et la dernière lettre.

### Exemple

```text
Nom : Nova

NOVA
nova
Nombre de lettres : 4
Première lettre : N
Dernière lettre : a
```

---

## Exercice 2 : Transmission extraterrestre

Une civilisation envoie un message.

Demandez un message et affichez :

- les 5 premiers caractères ;
- les 5 derniers caractères ;
- le message inversé.

### Exemple

```text
Message : bienvenue sur mars

Premiers caractères : bienv
Derniers caractères :  mars
Message inversé : sram rus eunevneib
```

---

## Exercice 3 : Recherche de signal

Demandez un message radio.

Vérifiez si le symbole `@` est présent.

### Exemple

```text
Message : SOS@MARS

Signal spécial détecté !
```

---

# 🛸 Niveau 2 - Les conditions

## Exercice 4 : Contrôle d'accès

Pour piloter un vaisseau, il faut avoir au moins 21 ans.

Demandez l'âge du pilote.

### Exemple

```text
Âge : 25

Accès autorisé.
```

```text
Âge : 18

Accès refusé.
```

---

## Exercice 5 : État du vaisseau

Demandez le pourcentage d'énergie du vaisseau.

Affichez :

- 80 à 100 → **Excellent**
- 40 à 79 → **Stable**
- 1 à 39 → **Critique**
- 0 → **Hors service**

### Exemple

```text
Énergie : 65

État : Stable
```

---

## Exercice 6 : La planète secrète

Le mot secret est :

```python
saturne
```

Si le joueur trouve le bon mot :

```text
Planète localisée !
```

Sinon :

```text
Coordonnées invalides.
```

---

# 🌌 Niveau 3 - Les listes

## Exercice 7 : Cargaison spatiale

Créez la liste suivante :

```python
["oxygène", "carburant", "nourriture"]
```

Affichez :

- le premier élément ;
- le dernier élément ;
- le nombre total d'éléments.

---

## Exercice 8 : Récolte d'astéroïdes

Créez une liste vide.

Demandez à l'utilisateur de saisir 5 minéraux trouvés sur différents astéroïdes.

Affichez ensuite tous les minéraux récoltés.

### Exemple

```text
Minéraux récoltés :
- Titane
- Fer
- Nickel
- Quartz
- Cobalt
```

---

## Exercice 9 : Analyse des planètes

Créez une liste contenant les températures suivantes :

```python
[-50, 15, 80, -120, 45]
```

Affichez :

- la température maximale ;
- la température minimale ;
- la température moyenne.

---

# 👽 Niveau 4 - Les ensembles (`set`)

## Exercice 10 : Catalogue extraterrestre

Liste observée :

```python
["zorg", "blip", "zorg", "xelon", "blip"]
```

Créez un `set` afin de conserver uniquement les espèces uniques.

### Résultat attendu

```python
{"zorg", "blip", "xelon"}
```

---

## Exercice 11 : Rencontre galactique

Deux explorateurs ont découvert des espèces.

```python
explorateur1 = {"zorg", "blip", "xelon"}
explorateur2 = {"xelon", "nova", "krill"}
```

Affichez :

- les espèces découvertes par les deux explorateurs ;
- toutes les espèces réunies.

---

## Exercice 12 : Inventaire scientifique

Demandez le nom de 10 échantillons collectés.

Utilisez un `set` afin d'afficher combien d'échantillons différents ont été trouvés.

---

# 🤖 Niveau 5 - Les dictionnaires (`dict`)

## Exercice 13 : Fiche du robot

Créez le dictionnaire suivant :

```python
robot = {
    "nom": "XR-3000",
    "énergie": 85,
    "planète": "Mars"
}
```

Affichez toutes les informations du robot.

---

## Exercice 14 : Base de données des planètes

Créez le dictionnaire suivant :

```python
planetes = {
    "Mercure": 58,
    "Vénus": 108,
    "Terre": 150,
    "Mars": 228
}
```

Les valeurs représentent la distance moyenne au Soleil (en millions de kilomètres).

Demandez le nom d'une planète et affichez sa distance.

Si la planète n'existe pas :

```text
Planète inconnue.
```

---

## Exercice 15 : Classement des pilotes

Créez le dictionnaire suivant :

```python
scores = {
    "Nova": 1250,
    "Orion": 980,
    "Vega": 2100,
    "Luna": 1850
}
```

Affichez :

- le pilote ayant le plus grand score ;
- son score.

---

# 🌠 Mission Finale : Gestion d'une expédition

Créez un programme qui :

1. Demande le nom du commandant.
2. Crée une liste vide pour les ressources.
3. Ajoute 3 ressources.
4. Vérifie si l'élément `"oxygène"` est présent.
5. Affiche les ressources sans doublons à l'aide d'un `set`.
6. Stocke toutes les informations dans un dictionnaire.

Exemple :

```python
equipage = {
    "commandant": "Nova",
    "niveau": 1,
    "ressources": [...]
}
```

7. Si le nombre de ressources est supérieur ou égal à 3 :

```text
Décollage autorisé !
```

Sinon :

```text
Ressources insuffisantes.
```

---

# 👑 Boss Final : Sauver la Station Spatiale

La station spatiale perd de l'altitude.

Créez un jeu où :

- l'ordinateur choisit un nombre aléatoire entre 1 et 50 ;
- ce nombre représente le code de stabilisation ;
- le joueur doit le trouver.

### Indices

Si le nombre est trop petit :

```text
Trop bas !
```

Si le nombre est trop grand :

```text
Trop haut !
```

Lorsque le joueur trouve :

```text
Station sauvée !
```

---

## ⭐ Bonus

Conservez dans une liste tous les essais du joueur et affichez :

- le nombre d'essais ;
- les valeurs déjà essayées ;
- toutes les valeurs uniques à l'aide d'un `set`.

---

## 🎯 Concepts pratiqués

- `str`
- `list`
- `set`
- `dict`
- `if / elif / else`
- conversion avec `int()`
- opérateurs de comparaison
- recherche dans une collection avec `in`
- fonctions intégrées (`min`, `max`, `len`, `sum`)
- module `random` (Boss Final)