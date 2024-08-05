import numpy as np
import matplotlib.pyplot as plt

delta_image = np.zeros((256, 256))
delta_image[64, 64] = 1

plt.title('Delta Function Image')
plt.imshow(delta_image, cmap='gray')
plt.show()