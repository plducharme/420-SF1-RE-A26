def ma_fonction(param1, param2):
    var = param1 * param2**2
    return var


print(ma_fonction(4, 5))
# var, param1, param2 n'existent pas en dehors de la fonction, elles sont locales à la fonction
print(var)

