import numpy as np

data = np.array(range(36), dtype=np.int8).reshape((4, 9))

print(data)
print()
data[1 : 3, 2 : 4] += 55
print(data)

