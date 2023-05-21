import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
data = np.random.randn(1000)

plt.hist(data, bins=30, color='skyblue', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()

