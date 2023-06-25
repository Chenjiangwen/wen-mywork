import numpy as np

a = np.arange(3,30,2)
print(a)
# kernel = np.array([[0.07511362,0.12384141,0.07511362],
#  [0.12384141,0.20417996,0.12384141],
#  [0.07511362,0.12384141,0.07511362]])
#
# img = np.array([[189,187,185],
#  [191,189,186],
#  [192,190,187]])
#
#
# h=img.shape[0] #矩阵的行数
# w=img.shape[1] #矩阵的列数
# print(h,w)
# img1=np.zeros((h,w)) #生成一个h行w列的0填充的矩阵
# #print(img1)
# for i in range (1,h-1):
#     for j in range (1,w-1):
#         sum=0
#         for k in range(-1,2):
#             for l in range(-1,2):
#                 sum+=img[i+k,j+l]*kernel[k+1,l+1]   #图像与卷积核进行卷积
#                 #print(img[i+k,j+l],kernel[k+1,l+1])
#         print(i,j,sum) #i=1,j=1,sum=188.526
#         print(img1[i,j]) #值为0
#         img1[i,j]=sum  #sum 赋给img1[i,j]为-68？？？？
#         print(img1[i,j])
#
# print(img1)

import cv2

import numpy as np
import math

# img=cv2.imread('image/girl_gray.png',cv2.IMREAD_COLOR)
# #ch1, ch2, ch3 = cv2.split(img)  # 拆分为 BGR 独立通道
# #img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
# cv2.imshow("original_img",img)
# if img.ndim == 2:
#     print("单通道灰度图")
# else:
#     print("多通道")
#
# cv2.imshow("img_new",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
