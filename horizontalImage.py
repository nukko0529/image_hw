import numpy as np
import matplotlib.pyplot as plt

horizontal_lines = np.zeros((256, 256))
horizontal_lines[::16, :] = 1

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.title('Horizontal Lines Image')
plt.imshow(horizontal_lines, cmap='gray')

plt.show()