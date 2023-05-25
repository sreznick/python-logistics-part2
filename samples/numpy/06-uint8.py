import numpy as np

data = np.array([1, 2], dtype=np.uint8)
print(data)
data[0] += 255
print(data) # [0, 2]

