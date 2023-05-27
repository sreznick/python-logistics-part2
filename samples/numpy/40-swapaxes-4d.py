import numpy as np

data = np.arange(120).reshape((2, 3, 4, -1))
print(data.shape)
print(data[0, 1, 2, 3])
print(np.swapaxes(data, 0, 2).shape)
print(np.swapaxes(data, 0, 2)[2, 1, 0, 3])

