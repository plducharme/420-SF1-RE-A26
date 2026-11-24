import matplotlib.pyplot as plt

coord_x = [1, 2, 3, 4, 5]
coord_y = [42, 30, 26, 7, 50]
y_carre_de_x = [x**2 for x in coord_x]

plt.plot(coord_x, coord_y, linestyle="--", color="red", marker="o")
plt.plot(coord_x, y_carre_de_x, color="darkgoldenrod", marker="^")
plt.title("Graphique d'exemple")
plt.xlabel("Axe des x")
plt.ylabel("Valeurs en y")
plt.legend(["x vs y", "y = x^2"])

plt.show()
