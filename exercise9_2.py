import numpy as np
import matplotlib.pyplot as plt

n = 100

# losowe punkty w [0,1]x[0,1]
x = np.random.rand(n)
y = np.random.rand(n)

# odległość od (0,0)
dist = np.sqrt(x**2 + y**2)

# kolory
colors = np.where(dist < 1, 'green', 'red')

# rozmiar punktów 
sizes = (np.abs(x) + np.abs(y)) * 200  # skalowanie dla lepszej widoczności

# wykres
plt.scatter(x, y, c=colors, s=sizes)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Random points in unit square")

plt.show()