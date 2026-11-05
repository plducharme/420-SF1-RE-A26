import pandas as pd
import matplotlib.pyplot as plt
# pandas est un package permettant de manipuler des données tabulaires

# Lecture du csv (similaire à une feuille excel)
# le retour donne un "dataframe", un tableau contenant les données
dataframe_jeux_videos = pd.read_csv("Video_Games.csv")

# affiche les infos sur le dataframe
dataframe_jeux_videos.info()

# retourne les données d'une colonne (Series)
series_platform = dataframe_jeux_videos["Platform"]

# On se fait un tuple vide
tuple_plateformes = ()

# On parcours la Series pour en extraire les plateformes uniques
for p in series_platform:
    if p in tuple_plateformes:
        continue
    else:
        tuple_plateformes = tuple_plateformes + (p, )

print(tuple_plateformes, f"longueur: {len(tuple_plateformes)}")

# On peut mettre une condition pour filtrer les données, ici on retourne seulement les lignes où la "Platform" est "PS3"
ventes_ps3 = dataframe_jeux_videos[dataframe_jeux_videos["Platform"] == "PS3"]

jeux_ps3 = ()
total_ventes_ps3_na = sum(ventes_ps3["NA_Sales"])
total_ventes_ps3_eu = sum(ventes_ps3["EU_Sales"])
total_ventes_ps3_jp = sum(ventes_ps3["JP_Sales"])


noms_jeux_ps3_series = ventes_ps3["Name"]
for nom in noms_jeux_ps3_series:
    jeux_ps3 = jeux_ps3 + (nom, )

print(jeux_ps3)
print(total_ventes_ps3_na)
print(total_ventes_ps3_eu)
print(total_ventes_ps3_jp)

regions_ventes = ("Amérique du Nord", "Union Européenne", "Japon")

plt.bar(regions_ventes, (total_ventes_ps3_na, total_ventes_ps3_eu, total_ventes_ps3_jp), color="r")
plt.title("Ventes PS3 par région")
plt.xlabel("Régions")
plt.ylabel("Ventes en millions")

plt.show()



