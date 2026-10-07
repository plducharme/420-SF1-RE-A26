# a et b sont des variables globales
a = 10
b = 20


def fonction():
    # x et y sont des variables locales à la fonction
    x = 30
    y = 40
    print("locals() = {0}".format(locals()))
    # Remarquez que x et y n'existent pas dans la portée globale
    print("globals() à l'intérieur de fonction() ", globals())
    print("*" * 80)


print("locals() = {0}".format(locals()))
print("*" * 80)
print("globals() = {0}".format(globals()))
print("*" * 80)

print("locals() == globals()?", locals() == globals())
print("*" * 80)

fonction()
