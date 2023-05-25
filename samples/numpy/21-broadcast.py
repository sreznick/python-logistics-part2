import numpy as np

data_1 = np.array(range(48), dtype=np.int8).reshape((6, 8))
data_2 = np.array(range(8), dtype=np.int8).reshape((8,))

print(data_1 + data_2)

