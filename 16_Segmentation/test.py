# import numpy as np
# import cv2
# from sklearn.cluster import MeanShift, estimate_bandwidth
# from skimage import io
# import matplotlib.pyplot as plt
# from scipy import ndimage
#
# # Read the image
# image_url = 'Images/COMP9517_23T2_Lab3_Images/Balls.png'
# image = io.imread(image_url)
#
# height, width, channels = image.shape
#
# # Reshape the image to a 2D array of pixels
# pixels = np.reshape(image, (height * width, channels))
#
#
# # Estimate the bandwidth for MeanShift
# bandwidth = estimate_bandwidth(pixels, quantile=0.01, n_samples=500)
#
# # Perform MeanShift clustering
# ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
# labels = ms.fit_predict(pixels)
#
# segmented_image = np.reshape(ms.cluster_centers_[labels], (height, width, channels))
#
# # Convert the segmented image to grayscale
# gray_segmented = cv2.cvtColor(segmented_image.astype(np.uint8), cv2.COLOR_BGR2GRAY)
#
# # Apply a binary threshold
# _, binary_segmented = cv2.threshold(gray_segmented, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#
# # Perform morphological operations
# kernel_segmented = np.ones((3, 3), np.uint8)
# closing_segmented = cv2.morphologyEx(binary_segmented, cv2.MORPH_CLOSE, kernel_segmented, iterations=2)
#
# # Find contours in the segmented image
# contours, _ = cv2.findContours(closing_segmented, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
# # Count the number of objects
# object_count = len(contours)
# print("Number of objects:", object_count)


import cv2
import numpy as np

# Read the image
image = cv2.imread('Images/COMP9517_23T2_Lab3_Images/Balls.png')

# Extract R, G, B channels
r, g, b = cv2.split(image)

# Flatten the color channels
r_flat = r.flatten()
g_flat = g.flatten()
b_flat = b.flatten()

# Stack the flattened channels
samples = np.column_stack((r_flat, g_flat, b_flat))


from sklearn.cluster import MeanShift

# Perform MeanShift clustering
ms = MeanShift()
predicted_labels = ms.fit_predict(samples)

# Reshape the predicted labels back into the original image dimensions
segmented_image = predicted_labels.reshape(image.shape[:2])

from skimage.measure import label

# Label the connected components
labels, num_objects = label(segmented_image, return_num=True)

print(f"Number of objects: {num_objects}")

