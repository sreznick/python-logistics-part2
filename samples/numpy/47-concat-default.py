import numpy as np

a = np.arange(10)
b = np.arange(5) + 100
c = np.arange(7) + 200
print(a.shape, b.shape, c.shape)
d = np.concatenate((a, b, c))
print(d.shape)
print(d)

