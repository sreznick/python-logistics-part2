import numpy as np

data_1 = np.array(range(36), dtype=np.int8).reshape((4, 9))
data_2 = np.array(range(36), dtype=np.int8).reshape((4, 9)) / 2

data = data_1 + data_2
print(data)

