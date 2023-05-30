import numpy as np

data1 = np.arange(6).reshape((2, 3))
data2 = np.arange(14).reshape((2, 7)) + 10
data3 = np.arange(9).reshape((3, 3))
data4 = np.arange(6).reshape((3, 2)) + 100
data5 = np.arange(15).reshape((3, 5)) + 1000

d = np.block([[data1, data2], [data3, data4, data5]])
print(d)

