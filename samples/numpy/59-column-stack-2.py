import numpy as np

a = np.array((1,2,3))
b = np.array([(2,3), (4, 5), (5, 6)])
print(a.shape, b.shape)

data = np.column_stack((a, b))
print(data.shape)
print(data)

