import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a.shape, b.shape)

data = np.dstack((a, b))
print(data.shape)
print(data)

