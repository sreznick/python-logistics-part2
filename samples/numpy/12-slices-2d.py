import numpy as np

data = np.array([[100, 12, 23, 200, 20, 10, 12, 8],
                 [1, 2, 3, 4, 11, 22, 33, 44],
                 [9, 8, 7, 6, 99, 88, 77, 66],
                ], dtype=np.int16)

print(data[1, 2])   # элемент
print(data[1, 2:5]) # вектор
print(data[1, 2:5].shape) # (3,)
print(data[1:2, 2]) # вектор
print(data[1:2, 2].shape) # (1,)
print(data[1:, 2:5].shape) # (2, 3)

