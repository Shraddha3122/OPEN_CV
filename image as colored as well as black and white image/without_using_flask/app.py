import cv2
import matplotlib.pyplot as plt

# Read the image in color and grayscale
color_image = cv2.imread("D:/WebiSoftTech/OPEN CV/image as colored as well as black and white image/taj1.jpg")
gray_image = cv2.imread("D:/WebiSoftTech/OPEN CV/image as colored as well as black and white image/taj1.jpg", cv2.IMREAD_GRAYSCALE)

# Convert BGR to RGB for correct color display in Matplotlib
color_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB)

# Display images using Matplotlib
plt.figure(figsize=(10, 5))

# Color Image
plt.subplot(1, 2, 1)
plt.imshow(color_image)
plt.title("Color Image")
plt.axis("off")

# Grayscale Image
plt.subplot(1, 2, 2)
plt.imshow(gray_image, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")

# Show the images
plt.show()

