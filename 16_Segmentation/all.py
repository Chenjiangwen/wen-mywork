import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage import io, color, filters, morphology, segmentation, feature
from scipy import ndimage
from sklearn.cluster import MeanShift, estimate_bandwidth
import pandas as pd

# Read the images
image_urls = ['Images/COMP9517_23T2_Lab3_Images/Balloons.png', 'Images/COMP9517_23T2_Lab3_Images/Balls.png', 'Images/COMP9517_23T2_Lab3_Images/Brains.png']
images = [io.imread(url) for url in image_urls]

# Part 1: MeanShift segmentation
segmented_images_meanshift = []

for image in images:
    height, width, channels = image.shape
    pixels = np.reshape(image, (height * width, channels))
    bandwidth = estimate_bandwidth(pixels, quantile=0.2, n_samples=500)  # Adjust quantile to 0.1
    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    labels = ms.fit_predict(pixels)
    segmented_image = np.reshape(ms.cluster_centers_[labels], (height, width, channels))
    segmented_images_meanshift.append(segmented_image)

# Part 2: Watershed segmentation
segmented_images_watershed = []

for image in images:
    gray = color.rgb2gray(image)
    threshold = filters.threshold_otsu(gray)
    binary = gray > threshold
    distance = ndimage.distance_transform_edt(binary)
    local_max = feature.peak_local_max(distance, labels=binary, min_distance=33, num_peaks=np.inf, exclude_border=False)  # Adjust min_distance to 15
    markers = np.zeros_like(distance, dtype=np.int32)
    markers[tuple(np.transpose(local_max))] = 1
    markers[~binary] = 2
    segmented = segmentation.watershed(-distance, markers, mask=binary)
    kernel = morphology.disk(3)
    segmented = morphology.dilation(segmented, kernel)
    segmented = morphology.erosion(segmented, kernel)
    segmented_images_watershed.append(segmented)

# Part 3: Count objects
def count_objects(segmented_image):
    labeled, num_objects = ndimage.label(segmented_image)
    return num_objects

mean_shift_counts = [count_objects(image) for image in segmented_images_meanshift]
watershed_counts = [count_objects(image) for image in segmented_images_watershed]

# Display the results in a table
data = {'Image': ['Balloons', 'Balls', 'Brains'],
        '#Objects MeanShift': mean_shift_counts,
        '#Objects Watershed': watershed_counts}

results_table = pd.DataFrame(data)
print(results_table)
