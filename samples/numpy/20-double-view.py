import numpy as np

data_1 = np.array(range(48), dtype=np.int16).reshape((6, 8))
data_2 = data_1[1:-1, 1:-1]
data_3 = data_2[1:-1, 1:-1]
data_3[0, 0] = 111
data_2[0, 0] = 222
data_1[0, 0] = 333

print(data_1)
print()
print(data_2)
print()
print(data_3)

