import numpy as np
import cv2
from sklearn.cluster import MeanShift, estimate_bandwidth
from skimage import io
import matplotlib.pyplot as plt

# Image file paths
image_directory = 'Images/COMP9517_23T2_Lab3_Images/'
image_names = ['Balloons.png', 'Balls.png', 'Brains.png']
num_images = len(image_names)

# Create a grid of subplots
fig, axs = plt.subplots(2, num_images, figsize=(15, 6))

# Loop through each image
for i, image_name in enumerate(image_names):
    # Read the image
    image_url = image_directory + image_name
    image = io.imread(image_url)

    # MeanShift clustering
    height, width, channels = image.shape
    pixels = np.reshape(image, (height * width, channels))
    bandwidth = estimate_bandwidth(pixels, quantile=0.2, n_samples=500)
    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    labels = ms.fit_predict(pixels)
    segmented_image = np.reshape(ms.cluster_centers_[labels], (height, width, channels))

    # Post-processing
    gray = cv2.cvtColor(segmented_image.astype(np.uint8), cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    kernel = np.ones((3, 3), np.uint8)
    closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel, iterations=2)
    masked_image = cv2.bitwise_and(segmented_image.astype(np.uint8), segmented_image.astype(np.uint8), mask=closing)

    # Display the original and segmented images
    axs[0, i].imshow(image)
    axs[0, i].set_title('Original Image: ' + image_name)
    axs[0, i].axis('off')
    axs[1, i].imshow(masked_image)
    axs[1, i].set_title('Segmented Image: ' + image_name)
    axs[1, i].axis('off')

# Adjust spacing between subplots
plt.tight_layout()

# Show all the images
plt.show()
