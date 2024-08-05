import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('photo_vertical48.jpg', 0)

f = np.fft.fft2(image)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20 * np.log(np.abs(fshift))

plt.subplot(1, 2, 1)
plt.title('Input Image')
plt.imshow(image, cmap='gray')
plt.subplot(1, 2, 2)
plt.title('Magnitude Spectrum')
plt.imshow(magnitude_spectrum, cmap='gray')
plt.show()