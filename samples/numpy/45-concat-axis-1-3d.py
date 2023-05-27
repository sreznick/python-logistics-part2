import numpy as np

a = np.arange(36).reshape((2, 3, 6))
b = np.arange(60).reshape((2, 5, 6)) + 100
print(a.shape, b.shape)

d = np.concatenate((a, b), axis=1)
print(d.shape)
print(d)

