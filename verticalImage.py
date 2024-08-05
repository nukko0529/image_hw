import numpy as np
import matplotlib.pyplot as plt

vertical_lines = np.zeros((256, 256))
vertical_lines[:, ::48] = 1

plt.figure(figsize=(10,5))

plt.title('Vertical Lines Image')
plt.imshow(vertical_lines, cmap='gray')

plt.show()