import cv2
import numpy as np
from skimage import io, color, filters, morphology, segmentation, feature
from scipy import ndimage
from sklearn.cluster import MeanShift, estimate_bandwidth
import pandas as pd

# Read the images
image_urls = ['Images/COMP9517_23T2_Lab3_Images/Balloons.png', 'Images/COMP9517_23T2_Lab3_Images/Balls.png',
              'Images/COMP9517_23T2_Lab3_Images/Brains.png']
images = [io.imread(url) for url in image_urls]

# Part 1: MeanShift segmentation
segmented_images_meanshift = []

# Loop through each image
for i, image_url in enumerate(image_urls):
    # 读取图像
    image = io.imread(image_url)

    # Step 1: Extract each colour channel
    red_channel = image[:, :, 0].flatten()
    green_channel = image[:, :, 1].flatten()
    blue_channel = image[:, :, 2].flatten()
    pixels = np.column_stack((red_channel, green_channel, blue_channel))

    # Step 2: Perform MeanShift clustering
    bandwidth = estimate_bandwidth(pixels, quantile=0.2, n_samples=1000)
    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    labels = ms.fit_predict(pixels)
    segmented_image = np.reshape(ms.cluster_centers_[labels], image.shape)

    # Step 3: Post-processing
    gray = cv2.cvtColor(segmented_image.astype(np.uint8), cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # Perform binary morphological operations
    kernel = np.ones((5, 5), np.uint8)
    closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel, iterations=2)
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel, iterations=2)

    # Apply the mask to the segmented image
    masked_image = cv2.bitwise_and(segmented_image.astype(np.uint8), segmented_image.astype(np.uint8), mask=opening)
    segmented_images_meanshift.append(masked_image)

    # num_objects, labeled_image = cv2.connectedComponents(opening)

# Part 2: Watershed segmentation
segmented_images_watershed = []

for image in images:
    gray = color.rgb2gray(image)
    threshold = filters.threshold_otsu(gray)
    binary = gray > threshold
    distance = ndimage.distance_transform_edt(binary)
    local_max = feature.peak_local_max(distance, labels=binary, min_distance=30, num_peaks=np.inf, exclude_border=False)
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
