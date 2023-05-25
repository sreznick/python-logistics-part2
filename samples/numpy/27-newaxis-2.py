import numpy as np

print(np.arange(100).shape)
print(np.arange(100)[10:20].shape)
print(np.arange(100)[10:20, np.newaxis].shape)
print(np.arange(100)[np.newaxis, 10:20].shape)

