import numpy as np

print(np.array([1, 10]).shape)
print(np.array([1, 10])[np.newaxis].shape)
print(np.array([1, 10])[np.newaxis, np.newaxis].shape)
print(np.array([1, 10])[np.newaxis, 0].shape)
print(np.array([1, 10])[0, np.newaxis].shape)

