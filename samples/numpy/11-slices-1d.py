import numpy as np

data = np.array([100, 12, 23, 200, 20, 10, 12, 8], dtype=np.int16)
print(data[1])   # элемент
print(data[2:5]) # вектор
print(data[2:5].shape) # (3,)
print(data[:].shape) # (8,)
print(data[2:2].shape) #  (0,)

