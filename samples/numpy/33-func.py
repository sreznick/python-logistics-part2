import numpy as np

data = np.arange(120).reshape((12, 10))
values = np.sin(data / 10.0)
print(values)

