import numpy as np

data = np.arange(36).reshape((4, -1))
print(data)
print()
print(np.transpose(data))
print()
print(data.T)
print()
data.T[0, 1] = 55
print(data)

