import numpy as np

data = np.array([
   [(123, 234, 120), (123, 45, 34), (34, 21, 12), (45, 54, 23)],
   [(32, 123, 222), (213, 123, 33), (12, 23, 34), (54, 34, 43)],
], dtype=np.float32)
coeffs = np.array([
   [0.2, 0.3, 0.45, 0.56],
   [0.21, 0.32, 0.43, 0.54],
], dtype=np.float32)

#print(data * coeffs) # так не заработает

print(data * coeffs.reshape((2, 4, 1)))

