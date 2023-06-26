import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color, filters, morphology, segmentation, feature
from scipy import ndimage

# Read the images
image_urls = ['Images/COMP9517_23T2_Lab3_Images/Balloons.png', 'Images/COMP9517_23T2_Lab3_Images/Balls.png', 'Images/COMP9517_23T2_Lab3_Images/Brains.png']
images = [io.imread(url) for url in image_urls]

# Perform operations on each image
segmented_images = []
for i, image in enumerate(images):
    # Convert the image to grayscale
    gray = color.rgb2gray(image)

    # Apply thresholding to create a binary image
    threshold = filters.threshold_otsu(gray)
    binary = gray > threshold

    # Calculate the distance transform
    distance = ndimage.distance_transform_edt(binary)

    # Find local maxima by applying a maximum filter to the distance transform
    local_max = feature.peak_local_max(distance, labels=binary, min_distance=33, num_peaks=np.inf, exclude_border=False)

    # Mark the background region as 0
    markers = np.zeros_like(distance, dtype=np.int32)
    markers[tuple(np.transpose(local_max))] = 1
    markers[~binary] = 2

    # Perform Watershed transformation
    segmented = segmentation.watershed(-distance, markers, mask=binary)

    # Perform morphological operations
    kernel = morphology.disk(3)
    segmented = morphology.dilation(segmented, kernel)
    segmented = morphology.erosion(segmented, kernel)

    # Append the segmented image to the list
    segmented_images.append(segmented)

    # Count the number of objects in the segmented image
    object_count = len(np.unique(segmented))
    print(object_count)
    if i >= len(images):
        print("Number of objects in Segmented Image", i - len(images) + 1, ":", object_count)

# Display the images
fig, axs = plt.subplots(2, 3, figsize=(15, 10))
axs = axs.flatten()

for i, ax in enumerate(axs):
    if i < len(images):
        ax.imshow(images[i])
        ax.set_title('Original Image')
    else:
        ax.imshow(segmented_images[i - len(images)], cmap='nipy_spectral')
        ax.set_title('Segmented Image')

    ax.axis('on')

plt.show()
