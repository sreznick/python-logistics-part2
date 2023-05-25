import numpy as np

data = np.array(range(36), dtype=np.int8).reshape((4, 3, 3))

data[1 : 3, 2, 2 : 3] = 55
print(data)

