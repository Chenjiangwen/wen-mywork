import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt
def creat_gauss_kernel(kernel_size, sigma):
    if sigma == 0:
        print('Error!The value of sigma cannot be zero.')
        sys.exit()
    gausskernel = np.zeros((kernel_size,kernel_size),np.float32)
    for i in range (kernel_size):
        for j in range (kernel_size):
            gausskernel[i,j] = 1 / (2 * np.pi * sigma ** 2) *np.exp(- ((i-1) ** 2 + (j-1) ** 2) / (2 * sigma ** 2))
    sum = np.sum(gausskernel)
    kernel = gausskernel/sum
    return kernel

def myfilter(img,kernel):
    h=img.shape[0] #矩阵的行数
    w=img.shape[1] #矩阵的列数
    #print(h,w)
    img1=np.zeros((h,w),np.uint8) #生成一个h行w列的0填充的矩阵
    #print(img1)
    for i in range (1,h-1):
        for j in range (1,w-1):
            sum=0
            for k in range(-1,2):
                for l in range(-1,2):
                    sum+=img[i+k,j+l]*kernel[k+1,l+1]   #图像与卷积核进行卷积
            img1[i,j]=sum
    return img1

def imageCompose(B,G,R):
    img_new = np.zeros((img.shape)).astype("uint8")
    img_new[:, :, 0] = B
    img_new[:, :, 1] = G
    img_new[:, :, 2] = R
    return img_new

img = cv2.imread('image\girl2.png')
cv2.imshow("original_img",img)
B, G, R = cv2.split(img)

kernel_size = 3
sigma = 1
kernel = creat_gauss_kernel(kernel_size,sigma)

B_new = myfilter(B,kernel)
G_new = myfilter(G,kernel)
R_new = myfilter(R,kernel)

gauss_img = imageCompose(B_new,G_new,R_new)

cv2.imshow("gauss",gauss_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
