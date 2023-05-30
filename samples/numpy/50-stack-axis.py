import numpy as np

a = np.arange(24).reshape(4, 6)

d = np.stack((a, a + 10, a + 20), axis=2)
print(d.shape)
print(d)

