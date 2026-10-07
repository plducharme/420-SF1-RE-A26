def fonction():
    global b
    print("premier print() fonction: b=", b)
    # a et c sont des variables locales à la fonction
    # pycharm averti que "a" a le même nom qu'une variable dans la portée globale ("shadows name from outer scope")
    a = 3
    c = 5
    b = b + c
    print("deuxième print() fonction: b=", b)
    print("print() fonction: a=", a)
    return a


a = 2
b = 2
print("print() avant la fonction: a=", a)
print("print() avant la fonction: b=", b)
fonction()
print("print() après la fonction: a=", a)
print("print() après la fonction: b=", b)
