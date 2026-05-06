import numpy as np
import matplotlib.pyplot as plt

# funkcja
def distance_sum(x, y):
    return np.sqrt((x + 1)**2 + y**2) + np.sqrt((x - 1)**2 + y**2)

# siatka punktów (grid)
x = np.linspace(-3, 3, 400)
y = np.linspace(-3, 3, 400)

X, Y = np.meshgrid(x, y)

# wartości funkcji
Z = distance_sum(X, Y)

# wizualizacja
plt.imshow(Z, extent=[-3, 3, -3, 3], origin='lower')
plt.colorbar(label="distance sum")
plt.title("Sum of distances to (-1,0) and (1,0)")
plt.xlabel("x")
plt.ylabel("y")

plt.show()