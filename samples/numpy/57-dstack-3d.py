import numpy as np

a = np.arange(24).reshape((2, 3, 4))
b = np.arange(30).reshape((2, 3, 5))
print(a.shape, b.shape)

data = np.dstack((a, b))
print(data.shape)
print(data)

