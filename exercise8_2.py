import numpy as np

v1 = np.array([10, 20, 30, 40, 50, 60])

v2 = v1[1::2]
v3 = v1[::-1]

print(v1)
print(v2)
print(v3)