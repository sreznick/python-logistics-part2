import numpy as np

data = np.array(range(24), dtype=np.int8)

print(data.reshape((2, 12)))
print(data.reshape((3, 8)))
print(data.reshape((4, 6)))
print(data.reshape((2, 3, 4)))
print(data.reshape((1, 2, 3, 4)))
print(data.reshape((2, 1, 3, 4)))

