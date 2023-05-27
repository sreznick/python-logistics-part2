import numpy as np

a = np.arange(36).reshape((2, 3, 6))
b = np.arange(18).reshape((2, 3, 3)) + 100
print(a.shape, b.shape)

d = np.concatenate((a, b), axis=2)
print(d.shape)
print(d)

