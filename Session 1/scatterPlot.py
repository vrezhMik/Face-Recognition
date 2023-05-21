import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = np.random.randint(10, 100, 50)

plt.scatter(x, y, c=colors, s=sizes, marker='o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot')
plt.grid(True)
plt.show()

