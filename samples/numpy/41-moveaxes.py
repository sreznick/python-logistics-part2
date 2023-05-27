import numpy as np

data = np.arange(72).reshape((4, 6, 3))
print(data.shape)
print(data[2, 3, :])
data_2 = np.moveaxes(data, [0, 1, 2], [1, 2, 0])
data_3 = np.moveaxes(data, [0, 1], [1, 2])

print(data_2.shape)
print(data_3.shape)

print(data_2[:, 2, 3])
print(data_3[:, 2, 3])

