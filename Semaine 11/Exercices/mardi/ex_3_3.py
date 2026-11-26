boutique = {'épée': 150, 'potion': 25, 'bouclier': 90, 'corde': 10}
panier = []

while True:

    article = input("Article : ")
    if article == "fin":
        break

    if article in boutique:
        panier.append(article)
    else:
        print("Le marchand n'a pas ça !")

total = 0

for a in panier:
    prix_article = boutique[a]
    total += prix_article

print(f"Panier : {panier} Total : {total} pièces d'or")
