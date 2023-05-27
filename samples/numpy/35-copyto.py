import numpy as np

data = np.arange(120).reshape((12, 10))
print(data)
print()
print(data[3:7, 2])
print()
np.copyto(data[2:5, 3:7], data[3:7, 2])
print(data)

