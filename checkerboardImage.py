import numpy as np
import matplotlib.pyplot as plt

checkerboard = np.indices((256, 256)).sum(axis=0) % 2

plt.title('Checkerboard Pattern')
plt.imshow(checkerboard, cmap='gray')
plt.show()