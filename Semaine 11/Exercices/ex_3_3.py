boutique = {'épée': 150, 'potion': 25, 'bouclier': 90, 'corde': 10}



panier = []
while True:

    item = input("Article : ")

    if item == "fin":
        # Le code avant le break pourrait être à l'extérieur de la boucle
        total = 0
        for i in panier:
            total += boutique[i]
        print(f"Panier : {panier} Total : {total} pièces d'or")
        break

    if item in boutique:
        panier.append(item)
    else:
        print("Le marchand n'a pas ça !")



# item = input("Article : ")
#
# while item != "fin":
#
#     # logique ici
#
#     item = input("Article : ")