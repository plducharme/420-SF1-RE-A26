import numpy as np
temperature = [-50, 15, 80, -12, 45]

print(f"Max: {max(temperature)}")
print(f"Min: {min(temperature)}")
print(f"Moyenne: {sum(temperature)/len(temperature)}")

print(f"Moy np: {np.mean(temperature)}")


