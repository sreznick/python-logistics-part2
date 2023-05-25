import numpy as np

data = np.array([100, 200, 20], dtype=np.int32)
v1 = data[0]
print(type(v1))
print(v1.dtype)
print(v1.shape)
v2 = data[1]
data2 = np.array([v1, v2])
print(data2.dtype) # np.float64
data2 = np.array([100, 200])
print(data2.dtype) # np.int32

