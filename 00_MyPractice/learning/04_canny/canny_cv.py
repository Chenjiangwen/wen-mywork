import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

pic = cv.imread('./image/girl2.png', 0)
a = cv.Canny(pic, 0, 50)
# cv.imshow('H,Gamma', np.hstack((pic, a)))

plt.figure()
plt.figure(figsize=(10, 8))
plt.subplot(122)
plt.title("Edge Detection")
plt.imshow(a, cmap="gray")
plt.subplot(121)
plt.title("Original")
plt.imshow(pic, cmap="gray")
# plt.savefig('./image/pretreatment_canny.png')
plt.pause(0.5)

