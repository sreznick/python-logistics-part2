import numpy as np

#print(np.array([[1, 2], [10, 15], [20, -9]]) + np.array([5, 2, 3]))  # не работает

#print(np.array([[1, 2], [10, 15], [20, -9]]) + np.array([[5, 2, 3]]))  # и так - тоже

print(np.array([[1, 2], [10, 15], [20, -9]]) + np.array([[5], [2], [3]]))  # а так - нормально

