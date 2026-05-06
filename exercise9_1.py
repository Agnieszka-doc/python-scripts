import numpy as np
import matplotlib.pyplot as plt

# zakres x
x = np.linspace(0, 10, 100)

# funkcje
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.exp(-x)

# wykresy
plt.plot(x, y1, color='red', linestyle='-', label='sin(x)')
plt.plot(x, y2, color='green', linestyle='--', label='cos(x)')
plt.plot(x, y3, color='blue', linestyle=':', label='exp(-x)')

# legenda
plt.legend()

plt.xlabel("x")
plt.ylabel("y")
plt.title("sin(x), cos(x), exp(-x)")

plt.show()