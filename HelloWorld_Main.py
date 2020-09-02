import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,3.14,500)
y = np.sin(x)*np.cos(x**2.)*np.cos(x)**2.0

plt.plot(x,y)
plt.grid()
plt.show()