import numpy as np

m1 = np.arange(1, 21).reshape(4, 5)
print(m1)
m2 = m1[:, ::-1]
print(m2)
m3 = m1[::-1, :]
print(m3)
m4 = m1[1:-1, 1:-1]
print(m4)
