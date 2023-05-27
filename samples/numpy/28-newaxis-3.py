import numpy as np

x = np.arange(5)
result = x[:, np.newaxis] + x[np.newaxis, :]
print(result)

