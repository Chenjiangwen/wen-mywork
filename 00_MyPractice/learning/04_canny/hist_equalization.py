import cv2
import matplotlib.pyplot as plt
import numpy as np

"""
第一步：读入图片
第二步：使用cv2.equalizeHist(img)均衡化像素
第三步：使用plt.hist 画出均衡化的直方图
第四步：使用plt.imshow 画出均衡化后的图像
这种全局的均衡化也会存在一些问题，由于整体亮度的提升，也会使得局部图像的细节变得模糊，因为我们需要进行分块的局部均衡化操作
"""

def gray(img):
    """
    Calculate function:
    Gray(i,j) = 0.299 * R(i,j) + 0.587 * G(i,j) + 0.114 * B(i,j)
    """
    # 读取图片
    # img = plt.imread(img_path)
    # 转换成 RGB 格式
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # 灰度化
    img_gray = np.dot(img_rgb[..., :3], [0.299, 0.587, 0.114])
    return img_gray

# 第一步：读入图片
img = cv2.imread('./image/girl2.png', 0)
# 第二步: 使用cv2.equalizeHist实现像素点的均衡化
ret = cv2.equalizeHist(img)

# 第三步：使用plt.hist绘制像素直方图
plt.subplot(121)
plt.hist(img.ravel(), 256)
plt.subplot(122)
plt.hist(ret.ravel(), 256)
plt.show()

# 第四步：使用cv2.imshow()绘值均衡化的图像
cv2.imshow('ret', np.hstack((img, ret)))
cv2.waitKey(0)

