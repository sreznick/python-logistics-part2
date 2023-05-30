import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 2000)

print(np.sin(x))

fig, ax = plt.subplots(layout='constrained')
ax.plot(x, np.sin(x), label='sin')
ax.plot(x, np.cos(x), label='cos')
ax.plot(x, np.sin(x) ** 2, label='sin^2')
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_title("Simple Plot")
ax.legend()

plt.show()

