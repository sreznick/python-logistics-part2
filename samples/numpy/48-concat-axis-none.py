import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
print(a.shape, b.shape)

d = np.concatenate((a, b), axis=None)
print(d.shape)
print(d)

