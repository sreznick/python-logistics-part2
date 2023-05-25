import numpy as np

data_1 = np.array(range(36), dtype=np.int16).reshape((4, 9))
data_2 = data_1[2:4]
data_3 = data_1[[2, 3]]



print(data_1.base)
print(data_2.base)
print(data_3.base)
print(np.array(range(36), dtype=np.int16).base)

