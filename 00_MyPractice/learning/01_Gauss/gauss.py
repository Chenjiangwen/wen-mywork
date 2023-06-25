import cv2
import sys

#from numpy import around
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np
import math

def creat_gauss_kernel(kernel_size, sigma):
    if sigma == 0:
        print('Error!The value of sigma cannot be zero.')
        sys.exit()
    gausskernel = np.zeros((kernel_size,kernel_size),np.float32)
    for i in range (kernel_size):
        for j in range (kernel_size):
            gausskernel[i,j] = math.fabs(1 / (2 * np.pi * sigma ** 2) *np.exp(- ((i-1) ** 2 + (j-1) ** 2) / (2 * sigma ** 2)))
    sum = np.sum(gausskernel)
    kernel = gausskernel/sum
    return kernel

def myfilter(img,kernel):
    h=img.shape[0] #矩阵的行数
    w=img.shape[1] #矩阵的列数
    #img1=np.zeros((h,w),np.uint8) #生成一个h行w列的0填充的矩阵，0黑色
    img1 = np.ones((h, w), np.uint8) *127 # 生成一个h行w列的每个元素为127填充的矩阵，127灰色
    #print(img1)
    for i in range (1,h-1):
        for j in range (1,w-1):
            sum=0
            for k in range(-1,2):
                for l in range(-1,2):
                    sum+=img[i+k,j+l]*kernel[k+1,l+1]   #图像与卷积核进行卷积
            img1[i,j]=sum
    return img1

#三个通道合成图像
def imageCompose(B,G,R):
    img_new = np.zeros((img.shape)).astype("uint8")
    img_new[:, :, 0] = B
    img_new[:, :, 1] = G
    img_new[:, :, 2] = R
    return img_new

def check(kernel_size,sigma,img):
    kernel = creat_gauss_kernel(kernel_size, sigma)
    # if img.ndim == 2:
    #     print("单通道灰度图")
    gauss_img = myfilter(img, kernel)
    #     cv2.imshow("1",gauss_img)
    #     print(gauss_img.shape)
    #sum = np.sum(gauss_img)/10000000
    # print(kernel_size,sum)

    return gauss_img


#加载图像拆分成三通道
#img = cv2.imread('image\girl_gray.png',-1)
img = cv2.imread('image/original/girl_gray.png', -1)
#cv2.imshow("original_img",img)
print(np.sum(img))
#转灰度图像
#img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# s3 = check(3,0.3,img)
# k5 = check(3,1.5,img)
k11 = check(41,1.5,img)
#
# if k3==k5==k7:
#     print("一样")
# else:
#     print("不一样")
# # print(a)
# fig = plt.figure()
# sub = fig.add_subplot(111)
#
# sub.plot(k3, color='orange')
# sub.plot(k5, color='blue')
# sub.legend(['kernel=3'], loc='upper right')
# plt.legend(['kernel=5'], loc='upper right')
# plt.show()

# arr_sigma = np.arange(1, 10,0.2)  #kernel=3
# arr_kernel = np.arange(3,42,2) #sigma = 1.5
#
# a = []
# for i in tqdm(range (len(arr_kernel))):
#     sum = check(arr_kernel[i],1.5,img)
#     # cv2.imwrite('image/sigma=1.5/kernel_' +str(arr_kernel[i])+'.png', pic)
#     a.append(sum)
# # print(a)
# plt.xlabel('Kernel',fontsize=14)
# plt.plot(arr_kernel,a,'-r*')
# plt.legend(['Sigma=1.5'], loc='upper right')
# plt.show()

# a = []
# for i in tqdm(range (len(arr_sigma))):
#     pic = check(3,arr_sigma[i],img)
#     cv2.imwrite('image/kernel=3/sigma_' +str(np.around(arr_sigma[i],1))+'.png', pic)

# if s1==s2==s3:
#     print("一样")
# else:
#     print("不一样")
# # print(a)
# fig = plt.figure()
# sub = fig.add_subplot(111)
#
# sub.plot(s1, color='orange')
# sub.plot(s2, color='blue')
# sub.legend(['kernel=3'], loc='upper right')
# plt.legend(['kernel=5'], loc='upper right')
# plt.show()

cv2.imshow('41',k11)
cv2.waitKey(0)
cv2.destroyAllWindows()

