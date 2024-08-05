import numpy as np
import matplotlib.pyplot as plt

random_image = np.random.rand(256, 256)

plt.title('Random Noise Image')
plt.imshow(random_image, cmap='gray')
plt.show()