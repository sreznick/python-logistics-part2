import numpy as np

data = np.arange(120).reshape((12, 10))
values = np.sin(data / 10.0)
p_pos = np.where(values > 0)
print(p_pos)

