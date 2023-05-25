import numpy as np

data = np.array([1, 2], dtype=np.int8)
print(data)
data += 127
print(data) # [-128, -127]

