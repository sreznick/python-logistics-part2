import numpy as np

a = np.arange(24).reshape(2, 3, 4)

d = np.stack((a, a + 10, a + 20))
print(d.shape)
print(d)

