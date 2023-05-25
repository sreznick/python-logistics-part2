import numpy as np

data_1 = np.array([11, 22, 33, 44, 55], dtype=np.int16)
data_2 = np.array([1, 2, 3, 4], dtype=np.int16).reshape((4, 1))

print(data_1 + data_2)

