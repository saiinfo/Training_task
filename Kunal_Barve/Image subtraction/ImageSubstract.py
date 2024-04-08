import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the input images
image1 = cv2.imread('Image-1.jpg')
image2 = cv2.imread('Image-2.jpg')

# Perform subtraction
sub = cv2.subtract(image1, image2)

# Display the images using matplotlib
plt.figure(figsize=(10, 6))

# Display Image 1
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title('Image 1')
plt.axis('off')

# Display Image 2
plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title('Image 2')
plt.axis('off')

# Display Subtracted Image
plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(sub, cv2.COLOR_BGR2RGB))
plt.title('Subtracted Image')
plt.axis('off')

plt.show()
