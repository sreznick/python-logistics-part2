import numpy as np

data = np.arange(120).reshape((2, 3, 4, -1))
print(data.shape)
print(data[0, 1, 2, 3])
print(data.T.shape)
print(data.T[3, 2, 1, 0])

