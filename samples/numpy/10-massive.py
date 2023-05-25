import numpy as np

data = np.array([100, 200, 20], dtype=np.int16)
print(data)
print(data + 1)
data += 2
print(data)
print(data)
data[:] = 11
print(data)
data = 1.23 # больше не ndarray
print(data)

