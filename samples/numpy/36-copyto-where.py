import numpy as np

data = np.sin(np.arange(48).reshape((8, 6)) * 3)
orig = data.copy()
data_2 = np.cos(np.arange(8).reshape((4, 2)))
target = data[3:7, 2:4]
print(target)
print()
print(data)
print()
np.copyto(target, data_2, where=target > 0)
print(data == orig)

