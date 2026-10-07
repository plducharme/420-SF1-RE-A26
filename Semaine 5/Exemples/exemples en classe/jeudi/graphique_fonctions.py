import matplotlib.pyplot as plt
import math

# Déclaration explicite
# coords_x = [1, 2, 3, 4, 5, 6]
# Version liste en compréhension
coords_x = [x for x in range(1, 11)]

y_lin = []
y_n_log_n = []
y_expo = []
y_poly = []


def lineaire(x):
    return x


def n_log_n(x):
    return x * math.log(x)


def expo(x):
    return 2**x


def polynomial(x):
    return x ** 2


for x in coords_x:
    y_lin.append(lineaire(x))

for x in coords_x:
    y_n_log_n.append(n_log_n(x))

for x in coords_x:
    y_expo.append(expo(x))

for x in coords_x:
    y_poly.append(polynomial(x))


# Couleur: https://matplotlib.org/stable/gallery/color/named_colors.html
# marker: https://matplotlib.org/stable/api/markers_api.html
plt.plot(coords_x, y_lin, color="darkmagenta", marker="h")
plt.plot(coords_x, y_n_log_n, color="springgreen", marker="X")
plt.plot(coords_x, y_expo, color="gold", marker="p")
plt.plot(coords_x, y_poly, color="red", marker="P")

plt.title("y en fonction de x")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["y = x", "y = x log x", "y = 2 ** x", "y = x**2"])

plt.show()




