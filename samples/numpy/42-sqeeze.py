import numpy as np

data = np.arange(72).reshape((4, 1, 6, 3))
print(data.shape)
print(np.squeeze(data).shape)

data = np.arange(1)
print(data.shape)
print(np.squeeze(data).shape)

