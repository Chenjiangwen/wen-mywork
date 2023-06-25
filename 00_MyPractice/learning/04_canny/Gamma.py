import cv2
import numpy as np

img = cv2.imread('image\\ret.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img = img/255.
img1 = np.power(img/float(np.max(img)), 1.5)

img2 = np.power(img/float(np.max(img)), 1/1.5)

#print(img1)
imgs = np.hstack((img, img1, img2))
cv2.imshow('org, gamma=1.5, gamma=1/1.5',imgs)
cv2.waitKey(0)
cv2.destroyAllWindows()