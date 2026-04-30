import numpy as np

# (a)
a = np.arange(0.0, 1.1, 0.1)

# (b)
b = np.zeros((5, 6), dtype=np.int8)

# (c)
x = complex(0, 1)
c = np.array([x**k for k in range(9)])

print(a)
print(b)
print(c)