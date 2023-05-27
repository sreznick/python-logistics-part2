import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
print(a.shape, b.shape)
c = np.concatenate((a, b), axis=0)
print(c.shape)
print(c)

