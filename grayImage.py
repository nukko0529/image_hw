import numpy as np
import matplotlib.pyplot as plt

gray_image = np.full((256, 256), 0.5)

plt.title('Gray Image')
plt.imshow(gray_image, cmap='gray')
plt.show()