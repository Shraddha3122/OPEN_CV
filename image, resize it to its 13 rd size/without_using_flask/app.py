import cv2
import matplotlib.pyplot as plt

# Load the image
image_path = "D:/WebiSoftTech/OPEN CV/image, resize it to its 13 rd size/without_using_flask/taj1.jpg"
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB for correct color representation

# Resize the image
height, width = image.shape[:2]
resized_image = cv2.resize(image, (width // 3, height // 3))

# Display the image using Matplotlib
plt.imshow(resized_image)
plt.axis("off")  # Hide axis
plt.show()
