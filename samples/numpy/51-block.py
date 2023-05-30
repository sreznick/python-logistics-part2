import numpy as np

data1 = np.arange(6).reshape((2, 3))
data2 = np.arange(10).reshape((2, 5)) + 10

d = np.block([data1, data2])
print(d)

