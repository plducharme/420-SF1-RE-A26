# Pour l'explication complète, voir tuple_extras.py

def somme_et_produit(x, y):
    return (x + y), (x * y)


# le tuple retourné ici est assigné à un tuple
tup = somme_et_produit(2, 3)
print(f"tup: {tup}")
# Le tuple retourné est "unpacked" dans les deux variables
somme, produit = somme_et_produit(5, 10)
print(f"la somme est {somme} et le produit est {produit}")


