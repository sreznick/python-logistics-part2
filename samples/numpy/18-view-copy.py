import numpy as np

data_1 = np.array(range(36), dtype=np.int8).reshape((4, 9))
data_2 = data_1[2:4]
data_3 = data_1[[2, 3]]

data_1[2, 0] = 77
data_2[0, 1] = 88 
data_3[0, 2] = 99

print(data_1)
print()
print(data_2)
print()
print(data_3)

