import numpy as np

print(np.arange(36).reshape((4, 9))[np.newaxis, 1:3].shape)
print(np.arange(36).reshape((4, 9))[1:2, np.newaxis, 1:3].shape)
print(np.arange(36).reshape((4, 9))[1:3, 2:5, np.newaxis].shape)
print(np.arange(36).reshape((4, 9))[np.newaxis, 2].shape)
print(np.arange(36).reshape((4, 9))[1, np.newaxis, 1:3].shape)
print(np.arange(36).reshape((4, 9))[1:2, np.newaxis, 2].shape)

