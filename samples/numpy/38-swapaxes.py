import numpy as np

data = np.arange(24).reshape((2, 3, -1))
print(data)
print()
print(np.swapaxes(data, 0, 1))
print()
print(data.T)
print()
data.T[0, 1] = 55
print(data)


