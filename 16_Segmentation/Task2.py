import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color, filters, morphology, segmentation, feature
from scipy import ndimage

# Read the images
image_urls = ['Images/COMP9517_23T2_Lab3_Images/Balloons.png', 'Images/COMP9517_23T2_Lab3_Images/Balls.png', 'Images/COMP9517_23T2_Lab3_Images/Brains.png']
images = [io.imread(url) for url in image_urls]

# Create a grid of subplots
fig, axs = plt.subplots(2, len(images), figsize=(15, 6))

# Perform operations on each image
for i, image in enumerate(images):
    # Step 1: Convert the image to grayscale and apply thresholding
    gray = color.rgb2gray(image)
    threshold = filters.threshold_otsu(gray)
    binary = gray > threshold

    # Apply binary morphological operations (e.g., opening)
    selem = morphology.disk(2)  # Define a disk-shaped structuring element with radius 2
    binary_opened = morphology.opening(binary, selem)

    # Step 2: Calculate the distance transform
    distance = ndimage.distance_transform_edt(binary_opened)

    # Step 3: Generate Watershed markers
    local_max = feature.peak_local_max(distance, labels=binary, min_distance=25, num_peaks=np.inf, exclude_border=False)
    markers = np.zeros_like(distance, dtype=np.int32)
    markers[tuple(np.transpose(local_max))] = 1
    markers[~binary] = 2

    # Step 4: Perform Watershed transformation
    segmented = segmentation.watershed(-distance, markers, mask=binary)

    # Perform binary morphological operations (optional)


    # Count the number of objects in the segmented image
    object_count = len(np.unique(segmented))
    axs[1, i].text(10, 20, f'Number of Objects: {object_count}', color='red')
    print(object_count)

    # Display the original and segmented images
    axs[0, i].imshow(image)
    axs[0, i].set_title('Original Image')
    axs[0, i].axis('off')
    axs[1, i].imshow(segmented, cmap='nipy_spectral')
    axs[1, i].set_title('Segmented Image')
    axs[1, i].axis('off')

# Adjust spacing between subplots
plt.tight_layout()

# Show all the images
plt.show()
